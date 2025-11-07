import re
from pathlib import Path

import numpy as np
import torch
from accelerate import PartialState
from peft import PeftModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer, BitsAndBytesConfig


# Path for pretrained model & tokenizer checkpoint
pretrained_checkpoint = "itskoma/biggitybiggityO"
# Make sure this is the same as in src/training/code/scripts/configs/config.checkpoint
base_checkpoint = "deepseek-ai/deepseek-coder-1.3b-base"
# Make sure this is the same as in src/training/code/scripts/data.id2label
id2label = {
    0: "O(1)",
    1: "O(logn)",
    2: "O(n)",
    3: "O(nlogn)",
    4: "O(n ^ 2)",
    5: "O(n ^ 3)",
    6: "np",
}
# Make sure this is the same as in src/training/code/scripts/evaluate.N_CLASSES
N_CLASSES = 7

BASE_LOCATION: Path = Path(__file__).parent


def set_model(checkpoint, tokenizer, ModelType=AutoModelForSequenceClassification):
    """Helper for setting up model"""

    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=dtype,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_storage=dtype,
    )

    # Load a pretrained model
    model = ModelType.from_pretrained(
        checkpoint,
        torch_dtype="auto",
        num_labels=N_CLASSES,
        trust_remote_code=True,
        device_map=PartialState().process_index,
        quantization_config=bnb_config,
        attn_implementation="flash_attention_2",  # Only for newer models
    )

    # Accomodating the size of the token embeddings for the potential missing <pad> token
    model.resize_token_embeddings(len(tokenizer), mean_resizing=False)

    # Passing the pad token id to the model config
    model.config.pad_token_id = tokenizer.pad_token_id
    return model


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
    # Loading pretrained tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(pretrained_checkpoint)
    # Base model
    base_model = set_model(base_checkpoint, tokenizer)
    # Load pretrained LoRA adapters on top
    model = PeftModel.from_pretrained(
        base_model, pretrained_checkpoint, dtype="auto", device_map="auto"
    )

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
    inputs = tokenizer(inputs, return_tensors="pt", padding=True, truncation=True).to(
        device=model.device
    )

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
