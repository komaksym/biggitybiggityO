import torch
from transformers import TrainingArguments

checkpoint = "deepseek-ai/deepseek-coder-1.3b-base"
experiment_name = "Full dataset focal loss testing"
batch_size = 4
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Training args
training_args = TrainingArguments(
    output_dir=f"training_results/{checkpoint}/",
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_strategy="epoch",
    # eval_steps=5,
    learning_rate=2e-4, # Testing
    bf16=True,
    # gradient_checkpointing=True,
    report_to="mlflow",
    num_train_epochs=5,
    max_grad_norm=0.3, # Per QLoRA paper recommendation
    warmup_ratio=0.03, # Per QLoRA paper recommendation
    weight_decay=0.001,
    lr_scheduler_type="cosine",
    label_names=["labels"],
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    gradient_accumulation_steps=4,
    load_best_model_at_end=True,
    run_name=f"{checkpoint}".split("/")[-1],
    # deepspeed="configs/ds_config.json",
)