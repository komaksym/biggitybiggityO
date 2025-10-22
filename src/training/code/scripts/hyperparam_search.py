import wandb
import optuna
from optuna.storages import RDBStorage
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification
from data import train_set, eval_set, tokenizer, data_collator
from evaluate import compute_metrics, ConfusionMatrixCallback, RecallScoreCallback, N_CLASSES
from configs.config import checkpoint
from peft import LoraConfig, get_peft_model


# Define persistent storage
storage = RDBStorage("sqlite:///optuna_trials.db")

# Init wandb
wandb.init(project="HPS-optuna", name="hyperparameter_search_optuna")


def objective(trial):
    """Optuna objective"""

    # Hyperparams to search
    learning_rate = trial.suggest_float("learning_rate", 2e-5, 4e-4, log=True)
    batch_size = trial.suggest_categorical("per_device_train_batch_size", [4, 8, 16])
    lora_rank = trial.suggest_categorical("r", [8, 16, 32, 64, 128])
    lora_alpha = trial.suggest_categorical("lora_alpha", [8, 16, 32, 64, 128])

    base_model = AutoModelForSequenceClassification.from_pretrained(
        checkpoint,
        torch_dtype="auto",
        num_labels=N_CLASSES,
        trust_remote_code=True,
        device_map="auto",
        attn_implementation="flash_attention_2",  # Only for newer models
    )

    # Accomodating the size of the token embeddings for the potential missing <pad> token
    base_model.resize_token_embeddings(len(tokenizer), mean_resizing=False)

    # Passing the pad token id to the model config
    base_model.config.pad_token_id = tokenizer.pad_token_id

    # LoRA config
    peft_config = LoraConfig(
        r=lora_rank,
        lora_alpha=lora_alpha,
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
        model = peft_model,
        args=training_args,
        train_dataset=train_set,
        eval_dataset=eval_set,
        data_collator=data_collator,
        processing_class=tokenizer,
        compute_metrics=compute_metrics,
        callbacks=[ConfusionMatrixCallback(), RecallScoreCallback()],
    )


    # Train
    trainer.train()

    results = trainer.evaluate()
    return results["eval_f1_macro"]

# Create study
study = optuna.create_study(
    study_name="hyperparam_search",
    direction="maximize",
    storage=storage,
    load_if_exists=True
)

study.optimize(objective, n_trials=10)
breakpoint()

