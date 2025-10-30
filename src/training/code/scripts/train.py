from .configs.config import checkpoint, training_args
from evaluate import ConfusionMatrixCallback, RecallScoreCallback, compute_metrics
from .model import set_model
from transformers import Trainer, BitsAndBytesConfig, AutoModelForSequenceClassification
from peft import LoraConfig, get_peft_model
import torch
from utils import setup_mlflow
import pandas as pd
from .data import find_paths, generate_prompt, set_tokenizer, tokenize_data, label2id
from datasets import Dataset
from .configs.config import DATASET_PATHS



def load_data(dataset_paths):
    """Finds paths to the datasets and loads them"""

    # Load paths up
    train_set_path, eval_set_path = find_paths(dataset_paths)

    # Read into pandas dataframes
    train_set = pd.read_csv(train_set_path)
    eval_set = pd.read_csv(eval_set_path)

    return train_set, eval_set

def preprocess_data(train_set, eval_set, tokenizer, label2id):
    """Applies prompting schema to the datasets, converts them to Dataset objects and tokenizes them"""

    # Apply instruction schema
    train_set = train_set.apply(generate_prompt, axis=1)
    eval_set = eval_set.apply(generate_prompt, axis=1)

    # Load as huggingface Datasets
    train_set = Dataset.from_pandas(train_set)
    eval_set = Dataset.from_pandas(eval_set)

     # Tokenize train/eval sets
    train_set = train_set.map(
        lambda x: tokenize_data(x, tokenizer, label2id),
        batched=True,
        remove_columns=train_set.column_names,
    )

    eval_set = eval_set.map(
        lambda x: tokenize_data(x, tokenizer, label2id),
        batched=True,
        remove_columns=eval_set.column_names,
    )

    return train_set, eval_set

def setup_model(tokenizer, checkpoint):
    # Bitsandbytes (Quantization)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_storage=torch.bfloat16,
    )

    # LoRA config
    peft_config = LoraConfig(
        r=32,
        lora_alpha=64,
        # target_modules = ['q_proj', 'v_proj'], # Qwen 
        target_modules="all-linear",  # Heavy, universal
        lora_dropout=0.05,
        bias="none",
        task_type="SEQ_CLS",  # might not work with this on
    )

    # Load the model
    base_model = set_model(checkpoint, tokenizer, AutoModelForSequenceClassification, bnb_config)

    # Wrap custom sequence classification head on top for deepseek v2 architecture (if using deepseek v2)
    #model = DeepseekV2ForSequenceClassification(model, model.config)
    # Apply LoRA
    peft_model = get_peft_model(model=base_model, peft_config=peft_config)

    # print(f"Model: {model}")
    # print(f"Model config: {model.config}")
    return peft_model

def main():
    # Set up tokenizer
    tokenizer, data_collator = set_tokenizer(checkpoint)

    # Load, preprocess, tokenize data
    train_set, eval_set = preprocess_data(load_data(DATASET_PATHS), tokenizer, label2id)

    # Setup model
    model = setup_model(tokenizer, checkpoint)

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_set,
        eval_dataset=eval_set,
        data_collator=data_collator,
        processing_class=tokenizer,
        compute_metrics=compute_metrics,
        callbacks=[ConfusionMatrixCallback(), RecallScoreCallback()],
    )
    # Setup experiment tracking
    setup_mlflow()

    # Train
    trainer.train()

    # Eval
    eval_metrics = trainer.evaluate(eval_dataset=eval_set)

    # Save metrics
    trainer.save_metrics(split="eval", metrics=eval_metrics)

    # Saving the full model if training with FSDP
    if trainer.is_fsdp_enabled:
        trainer.accelerator.state.fsdp_plugin.set_state_dict_type("FULL_STATE_DICT")

    # Save best model
    trainer.save_model(f"./best_model/{checkpoint}/")
    print("The best model was saved.")


if __name__ == "__main__":
    main()
