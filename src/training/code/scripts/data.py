import os
from pathlib import Path

import numpy as np
from transformers import AutoTokenizer, DataCollatorWithPadding


label2id = {"O(1)": 0, "O(logn)": 1, "O(n)": 2, "O(nlogn)": 3, "O(n ^ 2)": 4, "O(n ^ 3)": 5, "np": 6}
id2label = {label2id[k]: k for k in label2id.keys()}


def find_paths(dataset_paths):
    """Searches for paths and returns the train and eval set paths, raises error if none was found"""

    for path in dataset_paths:
        if os.path.exists(Path(dataset_paths[path]["train"]).exists()) and os.path.exists(
            Path(dataset_paths[path]["eval"])
        ):
            print("Data found!")
            return dataset_paths[path]["train"], dataset_paths[path]["eval"]

    raise FileNotFoundError(f"Datasets do not exist in the current paths: {dataset_paths}")


def generate_prompt(data_sample):
    """Defines prompt schema for instruction tuning"""

    data_sample["code"] = f"""
            Classify the code snippet into: O(1), O(logn), O(n), O(nlogn),
              O(n ^ 2), O(n ^ 3), np. And return the answer as the corresponding
                big O time complexity label.
            Code: {data_sample["code"]}"""

    return data_sample


def set_tokenizer(checkpoint):
    """Loads tokenizer from checkpoint, if tokenizer
    from checkpoint doesn't exist, it loads a base version of it"""

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


# Tokenization
def tokenize_data(data, tokenizer, label2id):
    """Tokenizes data and labels with the specified tokenizer"""
    tokenized = tokenizer(
        data["code"],
        truncation=True,
        max_length=512,
    )
    tokenized["labels"] = np.array([label2id[label] for label in data["complexity"]])
    return tokenized
