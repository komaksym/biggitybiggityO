
import numpy as np
import torch
from accelerate import PartialState
from peft import LoraConfig, get_peft_model
from sklearn.metrics import confusion_matrix, f1_score, recall_score
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    BitsAndBytesConfig,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
)

from data import load_dataset

# Quantization configuration (unchanged)
quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_storage=torch.bfloat16,
)

# Load the model with 4-bit quantization for sequence classification
model = AutoModelForSequenceClassification.from_pretrained(
    "facebook/opt-125m",
    quantization_config=quant_config,
    device_map=PartialState().process_index,
    torch_dtype=torch.bfloat16,
    num_labels=2,  # Binary classification (e.g., positive/negative for imdb)
)

# Apply LoRA for QLoRA (unchanged)
lora_config = LoraConfig(
    r=16, lora_alpha=32, target_modules="all-linear", lora_dropout=0.1, bias="none", task_type="SEQ_CLS"
)
model = get_peft_model(model, lora_config)

# Load and tokenize the dataset
dataset = load_dataset("imdb")  # imdb has 'train' and 'test' splits with text and labels
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m")


def tokenize_function(examples):
    # Tokenize text and include labels
    tokenized = tokenizer(examples["text"], truncation=True, max_length=512)
    tokenized["labels"] = examples["label"]
    return tokenized


def compute_metrics(eval_preds):
    logits, labels = eval_preds
    preds = np.argmax(logits[0], axis=-1) if isinstance(logits, tuple) else np.argmax(logits, axis=-1)

    # Calculate F-1 Macro
    f1_macro_score = f1_score(labels, preds, average="macro")

    # Calculate per-class recall
    recall_score_ = recall_score(labels, preds, average=None)

    # Calculate confusion matrix
    confusion_matrix_ = confusion_matrix(labels, preds)

    return {
        "f1_macro": f1_macro_score,
        "recall_score": recall_score_,
        "confusion_matrix": confusion_matrix_,
    }


# Map tokenization, removing original columns
tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=["text", "label"])

# Split dataset into train and evaluation sets, selecting 10 samples each
train_dataset = tokenized_dataset["train"].select(range(10))
eval_dataset = tokenized_dataset["test"].select(range(10))  # Using 'test' as eval set

# Data collator for sequence classification
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Training arguments (unchanged except for removing misplaced label_names)
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    eval_strategy="steps",
    save_strategy="steps",
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    gradient_accumulation_steps=1,
    learning_rate=2e-4,
    fp16=True,
    save_steps=200,
    eval_steps=200,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    logging_steps=200,
    report_to="none",
    label_names=["labels"],  # Specify labels for classification loss
)


# Create the Trainer with explicit label_names
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

# Train the model
trainer.train()

# Save metrics
test_metrics = trainer.evaluate(eval_dataset=eval_dataset)
trainer.save_metrics(split="test", metrics=test_metrics)

# Save the model
trainer.save_model("./best_model")
