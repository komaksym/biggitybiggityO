import torch
from data import id2label
import numpy as np
from model import base_model
from transformers import AutoTokenizer
from pathlib import Path
from peft import PeftModel

BASE_LOCATION: Path = Path(__file__).parent

def predict(inputs, model, tokenizer):
    # Tokenizing inputs
    inputs = tokenizer(inputs, return_tensors="pt", padding=True, truncation=True).to(device=model.device)

    # Predicting & decoding inputs
    preds = model(**inputs)
    logits = preds.logits[0].to(dtype=torch.float32).cpu().detach().numpy()
    preds = labelEncoder.inverse_transform(y=np.ravel(np.argmax(logits, axis=-1))) # Rewrite the encoder since i left labelEncoder behind

    return preds[0]


def main():
    test_sample = """
 def Onlogn_merge_sort(sequence):
    if len(sequence) < 2:
        return sequence
    
    m = len(sequence) // 2
    return Onlogn_merge(Onlogn_merge_sort(sequence[:m]), Onlogn_merge_sort(sequence[m:]))


def Onlogn_merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result
            """
    
    pretrained_path = BASE_LOCATION.parents[3] / "best_model/deepseek-ai/deepseek-coder-1.3b-base/"

    tokenizer = AutoTokenizer.from_pretrained(pretrained_path)
    model = PeftModel.from_pretrained(base_model, pretrained_path, dtype="auto", device_map="auto")

    response = predict(test_sample, model, tokenizer)
    print(f"LABEL: {response}")



if __name__ == "__main__":
    main()
