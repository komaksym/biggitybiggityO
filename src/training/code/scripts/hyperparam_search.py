import optuna
import torch
import wandb
import gc
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification, BitsAndBytesConfig
from data import train_set, eval_set, tokenizer, data_collator
from configs.config import checkpoint
from evaluate import compute_metrics, N_CLASSES
from peft import get_peft_model, LoraConfig

# Init wandb
wandb.init(project="HPS-optuna", name="hyperparameter_search_optuna")

# Bitsandbytes (Quantization)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_storage=torch.bfloat16,
)

def objective(trial):
    learning_rate = trial.suggest_float("learning_rate", 2e-5, 4e-4, log=True)
    batch_size = trial.suggest_categorical("per_device_train_batch_size", [4, 8, 16])

    # Model
    model = AutoModelForSequenceClassification.from_pretrained(
        checkpoint,
        torch_dtype="auto",
        num_labels=N_CLASSES,
        trust_remote_code=True,
        device_map="auto",
        quantization_config=bnb_config,
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

    model = get_peft_model(model, peft_config)


    # Training args
    training_args = TrainingArguments(
        output_dir=f"hps_results/{checkpoint}/",
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_strategy="epoch",
        learning_rate=2e-4, # Testing
        bf16=True,
        report_to="wandb",
        num_train_epochs=3,
        max_grad_norm=0.3, # Per QLoRA paper recommendation
        warmup_ratio=0.03, # Per QLoRA paper recommendation
        weight_decay=0.001,
        lr_scheduler_type="cosine",
        label_names=["labels"],
        load_best_model_at_end=True,
        run_name=f"{checkpoint}".split("/")[-1],
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_set,
        eval_dataset=eval_set,
        data_collator=data_collator,
        processing_class=tokenizer,
        compute_metrics=compute_metrics,
    )

    eval_result = trainer.evaluate()

    return eval_result["eval_f1_macro"]


# Create study
study = optuna.create_study(
    study_name="hyperparam_search",
    direction="maximize",
    load_if_exists=True
)
study.optimize(objective, n_trials=10)

