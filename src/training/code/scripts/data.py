import os
from pathlib import Path

from configs.config import checkpoint
from sklearn.preprocessing import LabelEncoder
from transformers import AutoTokenizer, DataCollatorWithPadding

from datasets import Dataset
import pandas as pd

BASE_LOCATION: Path = Path(__file__).parent

# Datasets
DATASET_PATHS = {
    "local": {
        "train": BASE_LOCATION.parents[3] / "train_set.csv",
        "eval": BASE_LOCATION.parents[3] / "eval_set.csv",
    },
    "local_two": {"train": "train_set.csv", "eval": "eval_set.csv"},
    "local_three": {
        "train": "drive/MyDrive/fine_tuning/train_set.csv",
        "eval": "drive/MyDrive/fine_tuning/eval_set.csv",
    },
    "kaggle": {
        "train": "/kaggle/input/python-codes-time-complexity/train_set.csv",
        "eval": "/kaggle/input/python-codes-time-complexity/eval_set.csv",
    },
}


def upload_datasets(dataset_paths=DATASET_PATHS):
    for path in dataset_paths:
        if os.path.exists(dataset_paths[path]["train"]) and os.path.exists(dataset_paths[path]["eval"]):
            print("Data found!")
            return dataset_paths[path]["train"], dataset_paths[path]["eval"]

    return FileNotFoundError(f"Datasets do not exist in the current paths: {dataset_paths}")


train_set_path, eval_set_path = upload_datasets()

# Read into pandas dataframes
train_set = pd.read_csv(train_set_path)
eval_set = pd.read_csv(eval_set_path)

def generate_prompt(data_sample):
    """Defines schema for instruction tuning"""

    data_sample["code"] = f"""
            Classify the code snippet into: O(1), O(logn), O(n), O(nlogn), O(n ^ 2), O(n ^ 3), np. And return the answer as the corresponding big O time complexity label.
            Code: {data_sample["code"]}"""

    #data_sample["complexity"] = f"""
    #Label: {data_sample["complexity"]}""".strip()

    return data_sample
    
# Apply instruction schema
train_set = train_set.apply(generate_prompt, axis=1)
eval_set = eval_set.apply(generate_prompt, axis=1)

# Fractionize for faster testing iterations
train_set = train_set.sample(frac=0.01)
eval_set = eval_set.sample(frac=0.01)

# Load as huggingface Datasets
train_set = Dataset.from_pandas(train_set)
eval_set = Dataset.from_pandas(eval_set)

# Tokenization
# Setting up Label Encoder
labelEncoder = LabelEncoder()
labelEncoder.fit(train_set["complexity"])


def tokenize_data(data, tokenizer):
    # Tokenizing
    tokenized = tokenizer(
        data["code"],
        truncation=True,
        max_length=512,
    )
    tokenized["labels"] = labelEncoder.transform(data["complexity"]) # Not sure if needed for the prompt schema
    return tokenized


def set_tokenizer(checkpoint):
    try:
        tokenizer = AutoTokenizer.from_pretrained(checkpoint, pad_token="<pad>")
    except Exception as e:
        print(f"Failed to load {checkpoint}: {e}")
        checkpoint = "-".join(checkpoint.split("-")[:2])
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        print(f"Falling back to {checkpoint}")

    X_train = train_set.map(
        lambda x: tokenize_data(x, tokenizer),
        batched=True,
        remove_columns=train_set.column_names,
    )
    X_eval = eval_set.map(
        lambda x: tokenize_data(x, tokenizer),
        batched=True,
        remove_columns=eval_set.column_names,
    )

    # Data Collator
    tokenizer.padding_side = "left"
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    return tokenizer, data_collator, X_train, X_eval


# Set up tokenizer, datasets, and model (as before)
tokenizer, data_collator, train_set, eval_set = set_tokenizer(checkpoint)
