# Installs
#pip install -U -q peft datasets bitsandbytes mlflow transformers accelerate


# # Imports
import pdb
import os
import torch
import torch.nn as nn
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, make_scorer
from datasets import load_dataset, Dataset
from transformers import AutoModel, AutoTokenizer, AutoModelForSequenceClassification, \
                        TrainingArguments, Trainer, DataCollatorWithPadding, BitsAndBytesConfig, \
                         AutoConfig, PreTrainedModel
from peft import LoraConfig, get_peft_model
from accelerate import FullyShardedDataParallelPlugin, Accelerator


# Datasets
DATASET_PATHS = {
    "local": {
        "train": "../../datasets/train_set.csv",
        "test": "../../datasets/test_set.csv"
    },
    "local_two": {
        "train": "train_set.csv",
        "test": "test_set.csv"
    },
    "local_three": {
        "train": "drive/MyDrive/fine_tuning/train_set.csv",
        "test": "drive/MyDrive/fine_tuning/test_set.csv"
    },

    "kaggle": {
        "train": "/kaggle/input/python-codes-time-complexity/train_set.csv",
        "test": "/kaggle/input/python-codes-time-complexity/test_set.csv"
    }
}


def upload_datasets(dataset_paths=DATASET_PATHS):
    for path in dataset_paths:
        if os.path.exists(dataset_paths[path]['train']) and os.path.exists(dataset_paths[path]['test']):
            return dataset_paths[path]['train'], dataset_paths[path]['test']

    return FileNotFoundError(f"Datasets do not exist in the current paths: {dataset_paths}")


train_set_path, test_set_path = upload_datasets()


LABELS_HIERARCHY = {
    'constant': 1,
    'logn': 2,
    'linear': 3,
    'nlogn': 4,
    'quadratic': 5,
    'cubic': 6,
    'np': 7
}


N_CLASSES = len(LABELS_HIERARCHY)


train_set = load_dataset("csv", data_files=train_set_path)['train']
eval_set = load_dataset("csv", data_files=test_set_path)['train']


# # Eval metrics
def hc_score(y_true, y_pred, n_classes=N_CLASSES):
    assert len(y_true) == len(y_pred), f"The amount of y_true labels: {len(y_true)} does not equal to the amount of y_pred: {len(y_pred)}."

    n_samples = len(y_true)

    return (np.sum(np.abs(y_pred - y_true)) / n_classes) / n_samples


def compute_metrics(eval_preds):
    logits, labels = eval_preds
    preds = np.argmax(logits[0], axis=-1) if isinstance(logits, tuple) else np.argmax(logits, axis=-1)

    # Calculate accuracy
    accuracy = accuracy_score(labels, preds)
    # Calculate F-1 Macro
    f1_macro_score = f1_score(labels, preds, average='macro')
    # Calculate Hierarchy Score
    hierarchy_score = hc_score(labels, preds)

    return {
        "accuracy": accuracy,
        "f1_macro": f1_macro_score,
        "hierarchy_score": hierarchy_score
    }

# Checkpoint
checkpoint = "gpt2"


# Tokenization
# Setting up Label Encoder
labelEncoder = LabelEncoder()
labelEncoder.fit(train_set['complexity'])

def tokenize_data(data, tokenizer):
    # Tokenizing
    tokenized = tokenizer(data['code'], truncation=True, max_length=512)
    tokenized['labels'] = labelEncoder.transform(data['complexity'])
    return tokenized


def set_tokenizer(checkpoint): 
    try:
        tokenizer = AutoTokenizer.from_pretrained(checkpoint, pad_token="<pad>")
    except Exception as e:
        print(f"Failed to load {checkpoint}: {e}")
        checkpoint = "-".join(checkpoint.split("-")[:2])
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        print(f"Falling back to {checkpoint}")

    X_train = train_set.map(
        lambda x: tokenize_data(x, tokenizer),
        batched=True,
        remove_columns=train_set.column_names
    )
    X_eval = eval_set.map(
        lambda x: tokenize_data(x, tokenizer),
        batched=True,
        remove_columns=eval_set.column_names
    )

    # Data Collator
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    return tokenizer, data_collator, X_train, X_eval


# Bitsandbytes (Quantization)
def setup_bnb_config():
    quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    )
    return quant_config


"""bnb_4bit_quant_type = 'nf4',
bnb_4bit_compute_dtype=torch.bfloat16,
bnb_4bit_use_double_quant=True,
bnb_4bit_quant_storage=torch.bfloat16"""


# Model loading
def set_model(checkpoint, tokenizer, ModelType=AutoModel):
    # Setup bitsandbytes quantization config
    quant_config = setup_bnb_config()

    # Load a pretrained model
    model = ModelType.from_pretrained(checkpoint, torch_dtype='auto', num_labels=7,
                                     trust_remote_code=True, 
                                     device_map='auto'
                                     )

    # Accomodating the size of the token embeddings for the potential missing <pad> token 
    model.resize_token_embeddings(len(tokenizer))

    # Passing the pad token id to the model config
    model.config.pad_token_id = tokenizer.pad_token_id
    return model


# PEFT (LoRA)
def setup_lora_config():
    lora_config = LoraConfig(
    #r=16,
    #lora_alpha=32,
    #target_modules = ['q_proj',  'v_proj'],
    target_modules = "all-linear",    
    lora_dropout=0.1,
    bias='none',
    task_type = "SEQ_CLS"
)
    return lora_config


# Training arguments
def set_training_args(checkpoint, batch_size=16):
    training_args = TrainingArguments(output_dir=f"training_results/{checkpoint}/",
                                    eval_strategy="epoch",
                                    logging_strategy="epoch",
                                    save_strategy="epoch",
                                    #eval_steps=2,
                                    #learning_rate=2e-4, # Testing
                                    bf16=True,
                                    report_to='mlflow',
                                    label_names=['labels'],
                                    num_train_epochs=3,
                                    warmup_steps=100, 
                                    per_device_train_batch_size=batch_size,
                                    per_device_eval_batch_size=batch_size // 2,
                                    gradient_accumulation_steps = 4,
                                    load_best_model_at_end=True,
                                    #pad_token="<pad>", # SFTTraianer
                                    #max_length=512 # SFTTrainer 
                                )
    return training_args


# Setup everything for training
def setup_training(checkpoint):
    # Set up tokenizer, datasets, and model (as before)
    tokenizer, data_collator, train_set, eval_set = set_tokenizer(checkpoint)

    model = set_model(checkpoint, tokenizer, AutoModelForSequenceClassification)

    """from peft import prepare_model_for_kbit_training
    model = prepare_model_for_kbit_training(model)"""
    
    # Wrapping in PEFT
    lora_config = setup_lora_config()
    model.add_adapter(lora_config)

    return model, data_collator, tokenizer, train_set, eval_set


# Launch
def finetune(checkpoint):
    # Set up tokenizer, datasets, and model (as before)
    model, data_collator, tokenizer, train_set, eval_set = setup_training(checkpoint)

    # Collecting
    training_args = set_training_args(checkpoint=checkpoint, batch_size=4)

    # Building  
    trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_set,
            eval_dataset=eval_set,
            data_collator=data_collator,
            tokenizer=tokenizer,
            compute_metrics=compute_metrics
        )
    
    # Train
    trainer.train()

    # Save metrics
    test_metrics = trainer.evaluate(eval_dataset=eval_set)
    trainer.save_metrics(split="test", metrics=test_metrics)


def main():
    finetune(checkpoint)


if __name__ == '__main__':
    main()
