from .data import tokenize_data, generate_prompt, label2id
from .evaluate import compute_metrics
from transformers import AutoTokenizer, Trainer
from pathlib import Path
from peft import PeftModel
from .model import set_model
import pandas as pd
from datasets import Dataset
from .configs.config import checkpoint

BASE_LOCATION: Path = Path(__file__).parent

def prep_data(data_path, tokenizer):
    # Load the data
    test_set = pd.read_csv(data_path)

    # Apply the prompt schema
    test_set = test_set.apply(generate_prompt, axis=1)
    # Convert to Dataset
    test_set = Dataset.from_pandas(test_set)

    # Tokenize
    test_set = test_set.map(
        lambda x: tokenize_data(x, tokenizer), batched=True, remove_columns=test_set.column_names
    )

def main():
    # Path for the pretrained model
    pretrained_path = BASE_LOCATION.parents[1] / "models/best_model/deepseek-ai/deepseek-coder-1.3b-base/"

    # Loading pretrained tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(pretrained_path)
    # Base model
    base_model = set_model(checkpoint, tokenizer)    
    # Load pretrained LoRA adapters on top
    model = PeftModel.from_pretrained(base_model, pretrained_path, dtype="auto", device_map="auto")

    # Specify the test set path
    try:
        test_set_path = BASE_LOCATION.parents[3] / "data/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial/test_set.csv"
    except:
        raise ValueError(f"Such path doesn't exist: {test_set_path}")

    # Read the test set
    test_set = pd.read_csv(test_set_path)
    # Apply the prompt schema
    test_set = test_set.apply(generate_prompt, axis=1)
    # Convert to Dataset
    test_set = Dataset.from_pandas(test_set)

    # Tokenize
    test_set = test_set.map(
        lambda x: tokenize_data(x, tokenizer, label2id), batched=True, remove_columns=test_set.column_names
    )

    # Init Trainer
    trainer = Trainer(
        model=model,
        processing_class=tokenizer,
        eval_dataset=test_set,
        compute_metrics=compute_metrics,
    )

    # Evaluate and save results
    results = trainer.evaluate()

    print(results)


if __name__ == "__main__":
    main()
