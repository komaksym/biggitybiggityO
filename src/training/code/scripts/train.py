from configs.config import checkpoint, training_args
from data import data_collator, eval_set, tokenizer, train_set
from evaluate import ConfusionMatrixCallback, RecallScoreCallback, compute_metrics
from model import peft_model
from transformers import Trainer
from utils import setup_mlflow

# Building
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


def main():
    # Setup experiment tracking
    setup_mlflow()

    # Train
    trainer.train()

    # Eval
    eval_metrics = trainer.evaluate(eval_dataset=eval_set)

    # Save metrics
    trainer.save_metrics(split="eval", metrics=eval_metrics)

    # Saving the full model if training with FSDP
    if trainer.is_fsdp_enabled:
        trainer.accelerator.state.fsdp_plugin.set_state_dict_type("FULL_STATE_DICT")

    # Save best model
    trainer.save_model(f"./best_model/{checkpoint}/")
    print("The best model was saved.")


if __name__ == "__main__":
    main()
