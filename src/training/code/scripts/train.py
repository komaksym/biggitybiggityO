from configs.config import training_args, checkpoint
from data import data_collator, eval_set, tokenizer, train_set
from model import model
from evaluate import ConfusionMatrixCallback, RecallScoreCallback, compute_metrics
from utils import setup_mlflow

from transformers import Trainer


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
