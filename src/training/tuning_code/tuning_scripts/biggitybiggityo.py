# Installs
# pip install -U peft datasets bitsandbytes mlflow
# pip install flash-attn --no-build-isolation

# Imports
import os
import pdb
from inspect import signature

import numpy as np
import torch
import torch.nn as nn
from accelerate import PartialState
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from sklearn.metrics import accuracy_score, f1_score, make_scorer, recall_score
from sklearn.preprocessing import LabelEncoder
from transformers import (
    AutoConfig,
    AutoModel,
    AutoModelForCausalLM,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    BitsAndBytesConfig,
    DataCollatorWithPadding,
    PreTrainedModel,
    Trainer,
    TrainingArguments,
)
from transformers.modeling_outputs import SequenceClassifierOutput

from datasets import Dataset, load_dataset

# Datasets
DATASET_PATHS = {
    "local": {
        "train": "../../datasets/train_set.csv",
        "test": "../../datasets/test_set.csv",
    },
    "local_two": {"train": "train_set.csv", "test": "test_set.csv"},
    "local_three": {
        "train": "drive/MyDrive/fine_tuning/train_set.csv",
        "test": "drive/MyDrive/fine_tuning/test_set.csv",
    },
    "kaggle": {
        "train": "/kaggle/input/python-codes-time-complexity/train_set.csv",
        "test": "/kaggle/input/python-codes-time-complexity/test_set.csv",
    },
}


def upload_datasets(dataset_paths=DATASET_PATHS):
    for path in dataset_paths:
        if os.path.exists(dataset_paths[path]["train"]) and os.path.exists(dataset_paths[path]["test"]):
            return dataset_paths[path]["train"], dataset_paths[path]["test"]

    return FileNotFoundError(f"Datasets do not exist in the current paths: {dataset_paths}")


train_set_path, test_set_path = upload_datasets()


LABELS_HIERARCHY = {
    "constant": 1,
    "logn": 2,
    "linear": 3,
    "nlogn": 4,
    "quadratic": 5,
    "cubic": 6,
    "np": 7,
}


N_CLASSES = len(LABELS_HIERARCHY)


train_set = load_dataset("csv", data_files=train_set_path)["train"]
eval_set = load_dataset("csv", data_files=test_set_path)["train"]


# # Eval metrics
def hc_score(y_true, y_pred, n_classes=N_CLASSES):
    assert len(y_true) == len(y_pred), (
        f"The amount of y_true labels: {len(y_true)} does not equal to the amount of y_pred: {len(y_pred)}."
    )

    n_samples = len(y_true)

    return (np.sum(np.abs(y_pred - y_true)) / n_classes) / n_samples


def compute_metrics(eval_preds):

    logits, labels = eval_preds
    preds = np.argmax(logits[0], axis=-1) if isinstance(logits, tuple) else np.argmax(logits, axis=-1)

    # Calculate F-1 Macro
    f1_macro_score = f1_score(labels, preds, average="macro")

    # Calculate per-class recall
    recall_score_ = recall_score(labels, preds, average=None)

    # Calculate confusion matrix
    #confusion_matrix = 

    # Calculate Hierarchy Score
    hierarchy_score = hc_score(labels, preds)

    return {
        "f1_macro": f1_macro_score,
        
        "recall_score": recall_score_,
        "hierarchy_score": hierarchy_score,
    }


# Tokenization
# Setting up Label Encoder
labelEncoder = LabelEncoder()
labelEncoder.fit(train_set["complexity"])


def tokenize_data(data, tokenizer):
    # Tokenizing
    tokenized = tokenizer(
        data["code"],
        truncation=True,
        max_length=512,
    )
    tokenized["labels"] = labelEncoder.transform(data["complexity"])
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
        remove_columns=train_set.column_names,
    )
    X_eval = eval_set.map(
        lambda x: tokenize_data(x, tokenizer),
        batched=True,
        remove_columns=eval_set.column_names,
    )

    # Data Collator
    tokenizer.padding_side = "left"
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    return tokenizer, data_collator, X_train, X_eval


# Bitsandbytes (Quantization)
def setup_bnb_config():
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_storage=torch.bfloat16,
    )
    return quant_config


# Model loading
def set_model(checkpoint, tokenizer, ModelType=AutoModel):
    # Setup bitsandbytes quantization config
    quant_config = setup_bnb_config()

    # Load a pretrained model
    model = ModelType.from_pretrained(
        checkpoint,
        torch_dtype=torch.bfloat16,
        num_labels=7,
        trust_remote_code=True,
        device_map=PartialState().process_index,
        quantization_config=quant_config,
        attn_implementation="flash_attention_2",
    )

    # Accomodating the size of the token embeddings for the potential missing <pad> token
    model.resize_token_embeddings(len(tokenizer), mean_resizing=False)

    # Passing the pad token id to the model config
    model.config.pad_token_id = tokenizer.pad_token_id
    return model


# Custom classifier head
class DeepseekV2ForSequenceClassification(PreTrainedModel):
    config_class = AutoConfig

    def __init__(self, base_model, config):
        super().__init__(config)
        self.num_labels = config.num_labels
        self.model = base_model

        self.dense = nn.Linear(config.n_embd, config.num_labels, bias=False, dtype=self.model.dtype)

        # Initialize weights and apply final processing
        self.post_init()

    def get_input_embeddings(self):
        return self.model.config.n_embd

    def forward(self, input_ids=None, attention_mask=None, labels=None, *args, **kwargs):
        outputs = self.model(input_ids, attention_mask)

        hidden_states = outputs.last_hidden_state
        logits = self.dense(hidden_states)

        # Batch size
        if input_ids is not None:
            batch_size = input_ids.shape[0]

        # If padding token id is not configured and the batch size is > 1
        if self.config.pad_token_id is None and batch_size != 1:
            raise ValueError("Cannot handle batch sizes > 1 if no padding token is defined.")
        # If padding token id is not configured
        if self.config.pad_token_id is None:
            last_non_pad_token = -1
        # if encoded inputs exist => find the last non padded token to pool data from
        elif input_ids is not None:
            non_pad_mask = (input_ids != self.config.pad_token_id).to(logits.device, dtype=torch.int32)
            token_indices = torch.arange(input_ids.shape[-1], device=logits.device, dtype=torch.int32)
            last_non_pad_token = (token_indices * non_pad_mask).argmax(-1)

        # Pooling logits from the last non padded token across the batches
        pooled_logits = logits[torch.arange(batch_size, device=logits.device), last_non_pad_token]

        # Calculating loss if labels are provided
        loss = None
        if labels is not None:
            loss = self.loss_function(
                logits=logits,
                labels=labels,
                pooled_logits=pooled_logits,
                config=self.config,
            )

        return SequenceClassifierOutput(loss=loss, logits=pooled_logits)


# LoRA config
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    # target_modules = ['q_proj', 'v_proj'], # Qwen
    target_modules="all-linear",  # Heavy, universal
    lora_dropout=0.1,
    bias="none",
    task_type="SEQ_CLS",  # might not work with this on
)


# Training args


def set_training_args(checkpoint, batch_size=16):
    training_args = TrainingArguments(
        output_dir=f"training_results/{checkpoint}/",
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_strategy="epoch",
        # eval_steps=5,
        # learning_rate=2e-4, # Testing
        bf16=True,
        gradient_checkpointing=True,
        report_to="mlflow",
        num_train_epochs=3,
        warmup_steps=100,  # Testing
        label_names=["labels"],
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        gradient_accumulation_steps=16,
        load_best_model_at_end=True,
        deepspeed="configs/ds_config.json",
    )
    return training_args


# Trainer
# Checkpoint
checkpoint = "codellama/CodeLlama-70b-Python-hf"


# Set up tokenizer, datasets, and model (as before)
tokenizer, data_collator, train_set, eval_set = set_tokenizer(checkpoint)
# train_set = train_set.select(range(100))
# eval_set = eval_set.select(range(100))

model = set_model(checkpoint, tokenizer, AutoModelForSequenceClassification)
# model = DeepseekV2ForSequenceClassification(model, model.config)
model = get_peft_model(model=model, peft_config=peft_config)

# pdb.set_trace()
print(f"Model: {model}")
# print(f"Model config: {model.config}")


# Collecting
training_args = set_training_args(checkpoint=checkpoint, batch_size=1)

# Building
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_set,
    eval_dataset=eval_set,
    data_collator=data_collator,
    processing_class=tokenizer,
    compute_metrics=compute_metrics,
)

# Train
trainer.train()

# Save metrics
test_metrics = trainer.evaluate(eval_dataset=eval_set)
trainer.save_metrics(split="test", metrics=test_metrics)

# Saving the full model
if trainer.is_fsdp_enabled:
    trainer.accelerator.state.fsdp_plugin.set_state_dict_type("FULL_STATE_DICT")

trainer.save_model(f"./best_model/{checkpoint}/")
print("The best model was saved.")
