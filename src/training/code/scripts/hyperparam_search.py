import optuna
import torch
import wandb
from evaluate import (
    N_CLASSES,
    ConfusionMatrixCallback,
    RecallScoreCallback,
    compute_metrics,
)
from joblib import parallel_config
from optuna.storages import RDBStorage
from peft import LoraConfig, get_peft_model
from transformers import (
    AutoModel,
    AutoModelForSequenceClassification,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
)

from .configs.config import DATASET_PATHS
from .data import label2id, set_tokenizer
from .model import DeepseekV2ForSequenceClassification
from .train import load_data, preprocess_data, setup_model

# Model
checkpoint = "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"

# Init wandb for tracking
wandb.init(project="HPS-optuna", name="hyperparameter_search_optuna")

# Define persistent storage
storage = RDBStorage("sqlite:///optuna_trials_deepseek-coder-v2.db")


def objective(trial):
    """Optuna objective"""

    # Hyperparameters grid to search
    hps_learning_rate = trial.suggest_float("learning_rate", 2e-5, 4e-4)
    hps_batch_size = trial.suggest_categorical("per_device_train_batch_size", [8, 16, 32])
    hps_lora_dropout = trial.suggest_float("lora_dropout", 0, 0.1)
    hps_weight_decay = trial.suggest_float("weight_decay", 0.01, 0.1)
    hps_warmup_ratio = trial.suggest_float("warmup_ratio", 0.01, 0.1)
    hps_lora_rank = trial.suggest_categorical("r", [32, 64, 128])
    hps_lora_alpha = trial.suggest_categorical("lora_alpha", [32, 64, 128])

    # Augmenting big batch size with gradient accum
    batch_size = 4
    gradient_accumulation_steps_ = hps_batch_size // batch_size

    # Bitsandbytes (Quantization)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_storage=torch.bfloat16,
    )

    # Load the pretrained model
    base_model = AutoModel.from_pretrained(
        checkpoint,
        torch_dtype="auto",
        num_labels=N_CLASSES,
        trust_remote_code=True,
        device_map="auto",
        attn_implementation="flash_attention_2",  # Only for newer models
        quantization_config=bnb_config,
    )

    # Accomodating the size of the token embeddings for the potential missing <pad> token
    base_model.resize_token_embeddings(len(tokenizer), mean_resizing=False)

    # Passing the pad token id to the model config
    base_model.config.pad_token_id = tokenizer.pad_token_id

    # LoRA config
    peft_config = LoraConfig(
        r=hps_lora_rank,
        lora_alpha=hps_lora_alpha,
        # target_modules = ['q_proj', 'v_proj'], # Qwen
        target_modules="all-linear",  # Heavy, universal
        lora_dropout=hps_lora_dropout,
        bias="none",
        task_type="SEQ_CLS",  # might not work with this on
    )

    # Apply custom classification head for Deepseek v2 architecture
    base_model = DeepseekV2ForSequenceClassification(base_model, base_model.config)

    # LoRA
    peft_model = get_peft_model(model=base_model, peft_config=peft_config)

    # Training args
    training_args = TrainingArguments(
        output_dir=f"hps_results/{checkpoint}/",
        save_strategy="no",
        learning_rate=hps_learning_rate,  # Testing
        bf16=True,
        num_train_epochs=3,
        max_grad_norm=0.3,  # Per QLoRA paper recommendation
        warmup_ratio=hps_warmup_ratio,  # Per QLoRA paper recommendation
        weight_decay=hps_weight_decay,
        lr_scheduler_type="cosine",
        report_to="wandb",
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        gradient_accumulation_steps=gradient_accumulation_steps_,
        label_names=["labels"],
        load_best_model_at_end=True,
        run_name=f"{checkpoint}".split("/")[-1],
    )

    # Trainer
    trainer = Trainer(
        model=peft_model,
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
    # Set up tokenizer
    tokenizer, data_collator = set_tokenizer(checkpoint)

    # Prep the data
    train_set, eval_set = preprocess_data(load_data(DATASET_PATHS), tokenizer, label2id)

    # Setup model
    model = setup_model(tokenizer, checkpoint)

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
