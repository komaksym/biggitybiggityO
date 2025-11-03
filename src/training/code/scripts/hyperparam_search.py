import optuna
from .evaluate import (
    ConfusionMatrixCallback,
    RecallScoreCallback,
    compute_metrics,
)
from joblib import parallel_config
from optuna.storages import RDBStorage
from transformers import (
    Trainer,
    TrainingArguments,
)
#import wandb
import torch

from .configs.config import DATASET_PATHS
from .data import label2id, set_tokenizer
from .train import load_data, preprocess_data, setup_model

# Model
checkpoint = "deepseek-ai/deepseek-coder-1.3b-base"

# Init wandb for tracking
#wandb.init(project="HPS-optuna", name="hyperparameter_search_optuna")

# Define persistent storage
storage = RDBStorage("sqlite:///optuna_trials_deepseek-coder-v2.db")


def objective(trial):
    """Optuna objective"""

    # Hyperparameters grid to search
    hps_learning_rate = trial.suggest_float("learning_rate", 2e-5, 4e-4)
    hps_batch_size = trial.suggest_categorical("per_device_train_batch_size", [8, 16, 32])
    trial.suggest_float("lora_dropout", 0, 0.1)
    hps_weight_decay = trial.suggest_float("weight_decay", 0.01, 0.1)
    hps_warmup_ratio = trial.suggest_float("warmup_ratio", 0.01, 0.1)
    trial.suggest_categorical("r", [32, 64, 128])
    trial.suggest_categorical("lora_alpha", [32, 64, 128])

    # Augmenting big batch size with gradient accum
    batch_size = 4
    gradient_accumulation_steps_ = hps_batch_size // batch_size

    # Set up tokenizer
    tokenizer, data_collator = set_tokenizer(checkpoint)

    # Prep the data
    train_set, eval_set = load_data(DATASET_PATHS)
    # Perform HPS only on 10% of the data
    train_set, eval_set = train_set.sample(frac=0.1), eval_set.sample(frac=0.1)
    # Preprocess the data
    train_set, eval_set = preprocess_data(train_set, eval_set, tokenizer, label2id)

    # Setup model
    model = setup_model(tokenizer, checkpoint)

    # Training args
    training_args = TrainingArguments(
        output_dir=f"hps_results/{checkpoint}/",
        save_strategy="no",
        learning_rate=hps_learning_rate,  # Testing
        bf16=True if torch.cuda.is_bf16_supported() else False,
        num_train_epochs=3,
        max_grad_norm=0.3,  # Per QLoRA paper recommendation
        warmup_ratio=hps_warmup_ratio,  # Per QLoRA paper recommendation
        weight_decay=hps_weight_decay,
        lr_scheduler_type="cosine",
        report_to="none",
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        gradient_accumulation_steps=gradient_accumulation_steps_,
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
        callbacks=[ConfusionMatrixCallback(), RecallScoreCallback()],
    )

    # Train
    trainer.train()

    # Run eval and save
    results = trainer.evaluate()
    return results["eval_f1_macro"]


if __name__ == "__main__":
        # Run each study in it's own python subprocess to avoid segfaults with bitsandbytes
    with parallel_config("multiprocessing"):
        # Create study
        study = optuna.create_study(
            study_name="hyperparam_search",
            direction="maximize",
            storage=storage,
            load_if_exists=True,
        )

        study.optimize(objective, n_trials=20)
