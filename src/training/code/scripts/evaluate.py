from train import trainer
from data import eval_set
from configs.config import checkpoint

# Save metrics
eval_metrics = trainer.evaluate(eval_dataset=eval_set)
trainer.save_metrics(split="eval", metrics=eval_metrics)

# Saving the full model
if trainer.is_fsdp_enabled:
    trainer.accelerator.state.fsdp_plugin.set_state_dict_type("FULL_STATE_DICT")

trainer.save_model(f"./best_model/{checkpoint}/")
print("The best model was saved.")
