from configs.config import checkpoint, batch_size
from data import data_collator, eval_set, tokenizer, train_set
from model import model
from utils import ConfusionMatrixCallback, RecallScoreCallback, compute_metrics, setup_mlflow

from transformers import Trainer, TrainingArguments

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
    report_to="mlflow",
    num_train_epochs=3,
    # warmup_steps=100,  # Testing
    label_names=["labels"],
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    gradient_accumulation_steps=1,
    load_best_model_at_end=True,
    run_name="full data 3 epochs",
    fsdp_config="configs/fsdp_config.yaml"
)

# Building
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


def main():
    # Setup experiment tracking
    setup_mlflow()

    # Train
    trainer.train()

    # Eval
    eval_metrics = trainer.evaluate(eval_dataset=eval_set)

    # Save metrics
    trainer.save_metrics(split="eval", metrics=eval_metrics)

    # Saving the full model
    if trainer.is_fsdp_enabled:
        trainer.accelerator.state.fsdp_plugin.set_state_dict_type("FULL_STATE_DICT")

    trainer.save_model(f"./best_model/{checkpoint}/")
    print("The best model was saved.")



if __name__ == "__main__":
    main()
