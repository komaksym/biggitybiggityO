import re

from pathlib import Path

import numpy as np
import torch
from peft import PeftModel
from transformers import AutoTokenizer

from ..training.code.scripts.configs.config import checkpoint
from ..training.code.scripts.data import id2label
from ..training.code.scripts.model import set_model



BASE_LOCATION: Path = Path(__file__).parent


def data_preprocessing(inputs):
    """Preprocesses data and applies instruction prompt"""

    def remove_comments(inputs: str) -> str:
        """Remove in-code comments."""

        return re.sub(
            r"(#.+?$)|([\"']{3,}.+?[\"']{3,})",
            "",
            inputs,
            flags=re.MULTILINE | re.DOTALL,
        )

    def strip_empty_lines(inputs: str) -> str:
        """
        Remove consecutive empty lines and keep only 1 between code lines.
        """

        filtered_code: list[str] = []

        for line in inputs.split("\n"):
            line: str = line.rstrip()

            if line == "":
                # If previous line is not another empty line
                if filtered_code and filtered_code[-1] != "":
                    filtered_code.append(line)
                else:
                    continue
            else:
                filtered_code.append(line)

        return "\n".join(filtered_code)
    
    def generate_prompt(inputs):
        """Defines prompt schema for instruction tuning"""

        inputs = f"""
                Classify the code snippet into: O(1), O(logn), O(n), O(nlogn),
                O(n ^ 2), O(n ^ 3), np. And return the answer as the corresponding
                    big O time complexity label.
                Code: {inputs}"""

        return inputs
    
    # Preprocess (remove comments)
    inputs = remove_comments(inputs)
    # Remove empty lines
    inputs = strip_empty_lines(inputs)
    # Generate a prompt
    inputs = generate_prompt(inputs)
    return inputs

def load_model_n_tokenizer():
    ## Path for the pretrained model
    pretrained_path = (
        BASE_LOCATION.parents[1] / "models/deepseek-ai/deepseek-coder-1.3b-base/"
    )
    assert pretrained_path.exists(), "Pretrained checkpoint does not exist"

    # Loading pretrained tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(pretrained_path)
    # Base model
    base_model = set_model(checkpoint, tokenizer)
    # Load pretrained LoRA adapters on top
    model = PeftModel.from_pretrained(base_model, pretrained_path, dtype="auto", device_map="auto")

    # Enable model eval mode to turn off dropout, grads, etc.
    model.eval()

    return model, tokenizer

def predict(inputs):
    """Predict and output the class"""

    # Load model and tokenizer
    model, tokenizer = load_model_n_tokenizer()

    # Preprocess the data
    inputs = data_preprocessing(inputs)

    # Run the pipeline
    inputs = tokenizer(inputs, return_tensors="pt", padding=True, truncation=True).to(device=model.device)

    # Predicting & decoding inputs
    preds = model(**inputs)
    logits = preds.logits[0].to(dtype=torch.float32).cpu().detach().numpy()
    label_id = np.ravel(np.argmax(logits, axis=-1))[0]
    pred = id2label[label_id]

    return pred


def main():
    inputs = """"
    # Sum of a Fibonacci series up to the nth term
        def o2n_fibonacci(n):
        '''Comments'''
            if n<2: # Comments
                return n #Comments	
            print("hello")
            return o2n_fibonacci(n-1) + o2n_fibonacci(n-2)
    """
    output = predict(inputs)
    print(f"Label: {output}")


if __name__ == "__main__":
    main()
