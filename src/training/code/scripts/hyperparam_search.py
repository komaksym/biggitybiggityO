import wandb
import optuna
import torch
from optuna.storages import RDBStorage
from transformers import Trainer, TrainingArguments, BitsAndBytesConfig, AutoModelForSequenceClassification
from data import train_set, eval_set, tokenizer, data_collator
from evaluate import compute_metrics, ConfusionMatrixCallback, RecallScoreCallback, N_CLASSES
from configs.config import checkpoint
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

# Bitsandbytes (Quantization)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_storage=torch.bfloat16,
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

def model_init():
    base_model = AutoModelForSequenceClassification.from_pretrained(
        checkpoint,
        torch_dtype="auto",
        num_labels=N_CLASSES,
        trust_remote_code=True,
        device_map="auto",
        quantization_config=bnb_config,
        #attn_implementation="flash_attention_2",  # Only for newer models
    )

    # Prep for LoRA
    base_model = prepare_model_for_kbit_training(base_model)
    # LoRA
    peft_model = get_peft_model(model=base_model, peft_config=peft_config)
    #peft_model = base_model

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
    return metrics["eval_f1_macro"]


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
            "per_device_train_batch_size", 1, 2,
        ),
        #"r": trial.suggest_int( # Lora rank
            #"r", 8, 128
        #),
        #"lora_alpha": trial.suggest_int(
            #"lora_alpha", 2, 512
        #)
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
