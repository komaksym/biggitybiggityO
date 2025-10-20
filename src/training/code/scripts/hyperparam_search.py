from model import peft_model
import wandb
import optuna
from optuna.storages import RDBStorage
from transformers import Trainer
from data import train_set, eval_set, tokenizer, data_collator
from evaluate import compute_metrics, ConfusionMatrixCallback, RecallScoreCallback

def model_init():
    return peft_model

# Define persistent storage
storage = RDBStorage("sqlite:///optuna_trials.db")

# Create study
study = optuna.create_study(
    study_name="hyperparam_search",
    direction="maximize",
    storage=storage,
    load_if_exists=True
)

# Init compute objective
def compute_objective(metrics):
    return metrics["f1_macro"]


# Init wandb
wandb.init(project="HPS-optuna", name="hyperparameter_search_optuna")

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
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    gradient_accumulation_steps=1,
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

# Define search space
def optuna_hp_space(trial):
    return {
        "learning_rate": trial.suggest_float("learning_rate", 2e-5, 4e-4, log=True),
        "per_device_train_batch_size": trial.suggest_int(
            "per_device_train_batch_size", 1, 32,
        ),
        "lora_rank": trial.suggest_int(
            "lora_rank", 8, 128
        ),
        "lora_alpha": trial.suggest_int(
            "lora_alpha", 2, 512
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
    storage="sqlite:///optuna_trials.db",
)

# Print the run results
print(best_run)
