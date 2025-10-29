import os
from pathlib import Path

import numpy as np
from configs.config import checkpoint, DATASET_PATHS
from transformers import AutoTokenizer, DataCollatorWithPadding
import pandas as pd

from datasets import Dataset


def find_paths(dataset_paths=DATASET_PATHS):
    """Searches for paths and returns the train and eval set paths, raises error if none was"""
    for path in dataset_paths:
        if os.path.exists(dataset_paths[path]["train"]) and os.path.exists(dataset_paths[path]["eval"]):
            print("Data found!")
            return dataset_paths[path]["train"], dataset_paths[path]["eval"]

    raise FileNotFoundError(f"Datasets do not exist in the current paths: {dataset_paths}")


train_set_path, eval_set_path = find_paths()

# Read into pandas dataframes
train_set = pd.read_csv(train_set_path)
eval_set = pd.read_csv(eval_set_path)


def generate_prompt(data_sample):
    """Defines prompt schema for instruction tuning"""

    data_sample["code"] = f"""
            Classify the code snippet into: O(1), O(logn), O(n), O(nlogn),
              O(n ^ 2), O(n ^ 3), np. And return the answer as the corresponding
                big O time complexity label.
            Code: {data_sample["code"]}"""

    return data_sample

# Apply instruction schema
train_set = train_set.apply(generate_prompt, axis=1)
eval_set = eval_set.apply(generate_prompt, axis=1)

# Load as huggingface Datasets
train_set = Dataset.from_pandas(train_set)
eval_set = Dataset.from_pandas(eval_set)

# Encoding labels
# Specifying the order of the labels
label2id = {'O(1)': 0, 'O(logn)': 1, 'O(n)': 2, 'O(nlogn)': 3, 'O(n ^ 2)': 4, 'O(n ^ 3)': 5, 'np': 6}
id2label = {label2id[k]: k for k in label2id.keys()}


# Tokenization
def tokenize_data(data, tokenizer):
    tokenized = tokenizer(
        data["code"],
        truncation=True,
        max_length=512,
    )
    tokenized["labels"] = np.array([label2id[label] for label in data["complexity"]]) # Not sure if needed for the prompt schema
    return tokenized


def set_tokenizer(checkpoint):
    try:
        tokenizer = AutoTokenizer.from_pretrained(checkpoint, pad_token="<pad>")
    except Exception as e:
        print(f"Failed to load {checkpoint}: {e}")
        checkpoint = "-".join(checkpoint.split("-")[:2])
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        print(f"Falling back to {checkpoint}")

    # Data Collator
    tokenizer.padding_side = "left"
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    return tokenizer, data_collator 


# Set up tokenizer
tokenizer, data_collator = set_tokenizer(checkpoint)

# Tokenize train/eval sets
train_set = train_set.map(
    lambda x: tokenize_data(x, tokenizer),
    batched=True,
    remove_columns=train_set.column_names,
    )

eval_set = eval_set.map(
    lambda x: tokenize_data(x, tokenizer),
    batched=True,
    remove_columns=eval_set.column_names,
)