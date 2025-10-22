import wandb
import optuna
import torch
from optuna.storages import RDBStorage
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification
from data import train_set, eval_set, tokenizer, data_collator
from evaluate import compute_metrics, ConfusionMatrixCallback, RecallScoreCallback, N_CLASSES
from configs.config import checkpoint
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training


# Define persistent storage
storage = RDBStorage("sqlite:///optuna_trials.db")

# Init wandb
wandb.init(project="HPS-optuna", name="hyperparameter_search_optuna")


def objective(trial):
    """Optuna objective""""

    # Hyperparams to search
    learning_rate = trial.suggest_float("learning_rate", 2e-5, 4e-4, log=True),
    batch_size = trial.suggest_categorical("per_device_train_batch_size", [4, 8, 16, 32])
    #lora_rank = trial.suggest_categorical("r", [8, 16, 32, 64, 128])
    #lora_alpha = trial.suggest_categorical("lora_alpha", [2, 32, 4, 64, 8, 128, 16, 256, 32, 512])

    base_model = AutoModelForSequenceClassification.from_pretrained(
        checkpoint,
        torch_dtype="auto",
        num_labels=N_CLASSES,
        trust_remote_code=True,
        device_map="auto",
        quantization_config=bnb_config,
        attn_implementation="flash_attention_2",  # Only for newer models
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

    # LoRA
    peft_model = get_peft_model(model=base_model, peft_config=peft_config)

    # Training args
    training_args = TrainingArguments(
        output_dir=f"hps_results/{checkpoint}/",
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_strategy="epoch",
        learning_rate=learning_rate, # Testing
        bf16=True,
        report_to="wandb",
        num_train_epochs=3,
        max_grad_norm=0.3, # Per QLoRA paper recommendation
        warmup_ratio=0.03, # Per QLoRA paper recommendation
        weight_decay=0.001,
        lr_scheduler_type="cosine",
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        gradient_accumulation_steps=1,
        label_names=["labels"],
        load_best_model_at_end=True,
        run_name=f"{checkpoint}".split("/")[-1],
    )

    # Trainer
    trainer = Trainer(
        args=training_args,
        train_dataset=train_set,
        eval_dataset=eval_set,
        data_collator=data_collator,
        processing_class=tokenizer,
        compute_metrics=compute_metrics,
        model_init=model_init,
        callbacks=[ConfusionMatrixCallback(), RecallScoreCallback()],
    )

# Create study
study = optuna.create_study(
    study_name="hyperparam_search",
    direction="maximize",
    storage=storage,
    load_if_exists=True
)


study.optimize(objective)

print(best_run)
