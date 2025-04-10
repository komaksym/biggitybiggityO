from model import (
    set_tokenizer,
    set_model,
    DeepseekV2ForSequenceClassification,
    set_training_args,
    config,
    checkpoint,
    get_peft_model,
    compute_metrics
)
from accelerate import Accelerator
from transformers import AutoModel, AutoTokenizer, AutoModelForSequenceClassification, \
                         TrainingArguments, Trainer, DataCollatorWithPadding, BitsAndBytesConfig

def setup_training(checkpoint):
    # Initialize Accelerator
    accelerator = Accelerator()

    # Set up tokenizer, datasets, and model (as before)
    tokenizer, data_collator, train_set, eval_set = set_tokenizer(checkpoint)
    base_model = set_model(checkpoint, tokenizer)
    model = DeepseekV2ForSequenceClassification(base_model, base_model.config)
    model = get_peft_model(model=model, peft_config=config)

    # Print trainable parameters
    model.print_trainable_parameters()

    # Prepare everything with Accelerator
    """model, train_set, eval_set, data_collator = accelerator.prepare(
        model, train_set, eval_set, data_collator
    )
    """
    return model, train_set, eval_set, data_collator, tokenizer


def train(checkpoint):
    # Setup training
    model, train_set, eval_set, data_collator, tokenizer = setup_training(checkpoint)

    # Collecting
    training_args = set_training_args(checkpoint=checkpoint, batch_size=16)

    # Building
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_set,
        eval_dataset=eval_set,
        data_collator=data_collator,
        tokenizer=tokenizer,
        compute_metrics=compute_metrics,
    )

    # Train
    trainer.train()

    # Save metrics
    test_metrics = trainer.evaluate(eval_dataset=eval_set)
    trainer.save_metrics(split="test", metrics=test_metrics)
    return trainer


def main():
    trainer = train(checkpoint)


if __name__ == "__main__":
    main()