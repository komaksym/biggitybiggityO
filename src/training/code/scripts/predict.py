from data import tokenizer
from datasts import Dataset
from train import trainer
from data import labelEncoder
import numpy as np
from model import model


def predict(inputs):
    # Tokenizing inputs
    test_sample = tokenizer(inputs, return_tensors="pt", padding=True, truncation=True)
    inputs = Dataset.from_dict({key: value.to(model.device) for key, value in test_sample.items()})

    # Predicting & decoding inputs
    preds = trainer.predict(test_dataset=inputs)
    preds = labelEncoder.inverse_transform(y=np.ravel(np.argmax(preds.predictions[0], axis=-1)))

    return preds


def main():
    test_sample = """
    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = {}
            for num in nums:
                count[num] = 1 + count.get(num, 0)

            arr = []
            for num, cnt in count.items():
                arr.append([cnt, num])
            arr.sort()

            res = []
            while len(res) < k:
                res.append(arr.pop()[1])
            return res
            """

    predict(test_sample)


if __name__ == "__main__":
    main()
