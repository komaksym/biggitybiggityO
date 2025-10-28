import torch
from data import id2label, generate_prompt, tokenize_data
from evaluate import compute_metrics
import numpy as np
from model import base_model
from transformers import AutoTokenizer, Trainer
from pathlib import Path
from peft import PeftModel
import pandas as pd
from datasets import Dataset

BASE_LOCATION: Path = Path(__file__).parent

def predict(inputs, model):
    # Predicting & decoding inputs
    preds = model(**torch.tensor(inputs.to_dict()))
    logits = preds.logits[0].to(dtype=torch.float32).cpu().detach().numpy()
    prediction = np.ravel(np.argmax(logits, axis=-1))[0]
    preds = id2label[prediction]

    return preds


def main():
    pretrained_path = BASE_LOCATION.parents[1] / "models/best_model/deepseek-ai/deepseek-coder-1.3b-base/"

    tokenizer = AutoTokenizer.from_pretrained(pretrained_path)
    model = PeftModel.from_pretrained(base_model, pretrained_path, dtype="auto", device_map="auto")
    # Read the test set
    test_set = pd.read_csv("test_set.csv")
    # Apply the prompt schema
    #test_set = test_set.apply(generate_prompt, axis=1)
    test_set = Dataset.from_pandas(test_set)

    # Tokenize
    test_set = test_set.map(
        lambda x: tokenize_data(x, tokenizer),
        batched=True,
        remove_columns=test_set.column_names
    )
    
    trainer = Trainer(
        model=model, 
        processing_class=tokenizer,
        eval_dataset=test_set,
        compute_metrics=compute_metrics
    )

    results = trainer.evaluate()

    print(results)



if __name__ == "__main__":
    main()
