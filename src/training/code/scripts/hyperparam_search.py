from model import peft_model
import wandb
import optuna
from optuna.storages import RDBStorage
from train import trainer

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
