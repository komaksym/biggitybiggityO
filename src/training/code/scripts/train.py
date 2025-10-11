import torch
import torch.nn.functional as F
from configs.config import checkpoint, training_args
from data import data_collator, eval_set, tokenizer, train_set
from evaluate import ConfusionMatrixCallback, RecallScoreCallback, compute_metrics
from model import model
from transformers import Trainer
from utils import setup_mlflow


class CustomLossTrainer(Trainer):
    def __init__(self, loss_fn=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store custom loss here
        # Should take (logits, labels) as args
        self.loss_fn = loss_fn

    def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
        # Assume labels is the name of the y ground truth
        labels = inputs.get("labels")
        outputs = model(**inputs)
        logits = outputs.get("logits")

        # Compute custom loss using our function
        loss = self.loss_fn(logits, labels)

        return (loss, outputs) if return_outputs else loss


# Implement Focal Loss
def focal_loss(logits, labels, gamma=2.0, alpha=0.25):
    # Compute cross entropy loss first
    ce_loss = F.cross_entropy(logits, labels, reduction='none')
    # Get probs
    probs = torch.exp(-ce_loss)
    # Compute focal loss
    focal_loss = alpha * (1 - probs) ** gamma * ce_loss

    return focal_loss


# Building
trainer = CustomLossTrainer(
    model=model,
    args=training_args,
    train_dataset=train_set,
    eval_dataset=eval_set,
    data_collator=data_collator,
    processing_class=tokenizer,
    compute_metrics=compute_metrics,
    loss_fn=focal_loss,
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
