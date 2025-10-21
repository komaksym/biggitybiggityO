import optuna
import torch
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification
from data import train_set, eval_set, tokenizer, data_collator
from configs.config import checkpoint
from evaluate import compute_metrics, N_CLASSES


def model_init():
    model = AutoModelForSequenceClassification.from_pretrained(
        checkpoint,
        torch_dtype="auto",
        num_labels=N_CLASSES,
        trust_remote_code=True,
        device_map="auto",
    )

    return model

# Create study
study = optuna.create_study(
    study_name="hyperparam_search",
    direction="maximize",
    load_if_exists=True
)

# Init compute objective
def compute_objective(metrics):
    return metrics["f1_macro"]


# Init wandb
#wandb.init(project="HPS-optuna", name="hyperparameter_search_optuna")

# Training args
training_args = TrainingArguments(
    output_dir=f"hps_results/{checkpoint}/",
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_strategy="epoch",
    learning_rate=2e-4, # Testing
    bf16=True,
    report_to="none",
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
    args=training_args,
    train_dataset=train_set,
    eval_dataset=eval_set,
    data_collator=data_collator,
    processing_class=tokenizer,
    compute_metrics=compute_metrics,
    model_init=model_init,
)

# Define search space
def optuna_hp_space(trial):
    return {
        "learning_rate": trial.suggest_float("learning_rate", 2e-5, 4e-4, log=True),
        "per_device_train_batch_size": trial.suggest_int(
            "per_device_train_batch_size", 4, 16,
        )
    }

# Start the run
best_run = trainer.hyperparameter_search(
    direction="maximize",
    backend="optuna",
    hp_space=optuna_hp_space,
    n_trials=10,
    compute_objective=compute_objective,
    study_name="optuna test run",
)

# Print the run results
print(best_run)
