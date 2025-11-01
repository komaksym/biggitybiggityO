import torch
from transformers import TrainingArguments
from pathlib import Path

# File base location
BASE_LOCATION: Path = Path(__file__).parent

# Dataset paths
DATASET_PATHS = {
    "local": {
        "train": BASE_LOCATION.parents[4]
        / "data/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial"
        / "train_set.csv",
        "eval": BASE_LOCATION.parents[4]
        / "data/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial"
        / "eval_set.csv",
    },
    "local_two": {"train": "train_set.csv", "eval": "eval_set.csv"},
    "local_three": {
        "train": "drive/MyDrive/fine_tuning/train_set.csv",
        "eval": "drive/MyDrive/fine_tuning/eval_set.csv",
    },
    "kaggle": {
        "train": "/kaggle/input/python-codes-time-complexity/train_set.csv",
        "eval": "/kaggle/input/python-codes-time-complexity/eval_set.csv",
    },
}

# Checkpoint
checkpoint = "deepseek-ai/deepseek-coder-1.3b-base"
# Experiment name for MLFlow
experiment_name = "Test training post minor refactoring"

# Batch size & grad accumulation steps
effective_batch_size = 16
batch_size = 8
grad_accum_steps = effective_batch_size // batch_size

# Device (cpu/gpu)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Training args for transformers.Trainer
training_args = TrainingArguments(
    output_dir=f"training_results/{checkpoint}/",
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_strategy="epoch",
    learning_rate=2e-4,  # Testing
    bf16=True if torch.cuda.is_bf16_supported() else False,
    # gradient_checkpointing=True,
    report_to="mlflow",
    num_train_epochs=3,
    max_grad_norm=0.3,  # Per QLoRA paper recommendation
    warmup_ratio=0.03,  # Per QLoRA paper recommendation
    weight_decay=0.001,
    lr_scheduler_type="cosine",
    label_names=["labels"],
    per_device_train_batch_size=batch_size,  # should be 16
    per_device_eval_batch_size=batch_size,
    gradient_accumulation_steps=grad_accum_steps,
    load_best_model_at_end=True,
    run_name=f"{checkpoint}".split("/")[-1],
    # deepspeed="configs/ds_config.json",
)
