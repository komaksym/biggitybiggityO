import torch
from transformers import TrainingArguments

checkpoint = "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"
run_name = "Deepseek vs Qwen 17/33B vs 30B"
batch_size = 2
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Training args
training_args = TrainingArguments(
    output_dir=f"training_results/{checkpoint}/",
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_strategy="epoch",
    # eval_steps=5,
    # learning_rate=2e-4, # Testing
    bf16=True,
    # gradient_checkpointing=True,
    #report_to="mlflow",
    num_train_epochs=1,
    # warmup_steps=100,  # Testing
    label_names=["labels"],
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    gradient_accumulation_steps=8,
    load_best_model_at_end=True,
    run_name=f"{checkpoint}".split("/")[-1],
    # deepspeed="configs/ds_config.json",
)