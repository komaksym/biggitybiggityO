import torch
from transformers import TrainingArguments

checkpoint = "Qwen/Qwen3-Coder-30B-A3B-Instruct"
experiment_name = "Finetuning post HPS"

# Batch size
effective_batch_size = 32
batch_size = 8
grad_accum_steps = effective_batch_size / batch_size

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
    num_train_epochs=7,
    max_grad_norm=0.3, # Per QLoRA paper recommendation
    warmup_ratio=0.03, # Per QLoRA paper recommendation
    weight_decay=0.001,
    lr_scheduler_type="cosine",
    label_names=["labels"],
    per_device_train_batch_size=batch_size, # should be 16
    per_device_eval_batch_size=batch_size,
    gradient_accumulation_steps=grad_accum_steps,
    load_best_model_at_end=True,
    run_name=f"{checkpoint}".split("/")[-1],
    # deepspeed="configs/ds_config.json",
)