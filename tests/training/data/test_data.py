from pathlib import Path

import great_expectations as gx
import pandas as pd
import pytest
from datasets import Dataset
from transformers.data.data_collator import DataCollatorWithPadding
from transformers.models.llama.tokenization_llama_fast import LlamaTokenizerFast
from transformers.models.qwen2.tokenization_qwen2_fast import Qwen2TokenizerFast
from transformers import AutoTokenizer

from src.training.code.scripts.data import (
    find_paths,
    generate_prompt,
    set_tokenizer,
    tokenize_data,
    label2id
)

BASE_LOCATION = Path(__file__).parent


@pytest.fixture(scope="module")
def df_path():
    return (
        BASE_LOCATION.parents[2]
        / "data/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial/full_no_exponential+factorial.csv"
    )


@pytest.fixture(scope="module")
def df(df_path):
    return pd.read_csv(df_path)


@pytest.fixture(scope="module")
def tokenizer_path():
    return BASE_LOCATION.parents[2] / "src/training/models/best_model/deepseek-ai/deepseek-coder-1.3b-base/"


@pytest.fixture(scope="module")
def tokenizer(tokenizer_path):
    return AutoTokenizer.from_pretrained(tokenizer_path)


def test_dataset(df):
    """Test dataset quality and integrity"""

    # Set up metadata keeper
    context = gx.get_context()

    # Setup data source and data asset to work with
    data_source = context.data_sources.add_pandas("pandas")
    data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

    # Add batch definition
    batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
    # Add batch, which will be validated
    batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

    # Create an Expectation Suite
    expectation_suite_name = "bigO_time_complexity_suite"
    suite = gx.ExpectationSuite(name=expectation_suite_name)

    # Add Expectations
    column_list = ["code", "complexity"]
    suite.add_expectation(
        gx.expectations.ExpectTableColumnsToMatchOrderedList(column_list=column_list)
    )
    complexities = ["O(1)", "O(logn)", "O(n)", "O(nlogn)", "O(n ^ 2)", "O(n ^ 3)", "np"]
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeInSet(
            column="complexity", value_set=complexities
        )
    )
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="code"))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="code"))
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="complexity")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="code", type_="str")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeOfType(column="complexity", type_="str")
    )

    # Add the Expectation Suite to Context
    context.suites.add(suite)

    # Validate the Data against the Suite
    validation_results = batch.validate(suite)
    # Validate
    assert validation_results["success"]


@pytest.fixture
def dataset_paths():
    """Real set of data paths"""

    DATASET_PATHS = {
        "local": {
            "train": BASE_LOCATION.parents[2]
            / "data/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial"
            / "train_set.csv",
            "eval": BASE_LOCATION.parents[2]
            / "data/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial"
            / "eval_set.csv",
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
    return DATASET_PATHS


@pytest.fixture
def expected_data_paths():
    """Expected data to get from testing find_paths function"""

    return Path(
        "/Users/koval/dev/biggitybiggityO/data/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial/train_set.csv"
    ), Path(
        "/Users/koval/dev/biggitybiggityO/data/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial/eval_set.csv"
    )


def test_find_paths(dataset_paths, expected_data_paths):
    """Testing find_paths function"""

    # Load paths up
    train_set_path, eval_set_path = find_paths(dataset_paths)
    # Evaluate
    assert train_set_path, eval_set_path == expected_data_paths


@pytest.fixture
def expected_prompt():
    return "\n            Classify the code snippet into: O(1), O(logn), O(n), O(nlogn),\n              O(n ^ 2), O(n ^ 3), np. And return the answer as the corresponding\n                big O time complexity label.\n            Code: from math import sqrt\n\na, v = map(int, input().split())\nl, d, w = map(int, input().split())\n\ndef findt(u, v, a, dist):\n\tfront = (v*v-u*u)/(2*a)\n\tif front > dist:\n\t\treturn (sqrt(u*u+2*a*dist)-u)/a\n\treturn (v-u)/a + (dist-front)/v\n\ndef solve(a, v, l, d, w):\n\tif v <= w or 2*a*d <= w*w:\n\t\treturn findt(0, v, a, l)\n\tafter = findt(w, v, a, l-d)\n\tpeak = sqrt(a*d + w*w/2)\n\tif peak > v:\n\t\ttravel = (v*v-w*w/2)/a\n\t\tbefore = (2*v-w)/a + (d-travel)/v\n\telse:\n\t\tbefore = (2*peak-w)/a\n\treturn before + after\n\nprint(f'{solve(a, v, l, d, w):.8f}')"


def test_generate_prompt(df, expected_prompt):
    sample_to_test = df.iloc[:1]
    got = sample_to_test.apply(generate_prompt, axis=1)
    assert got["code"].iloc[0] == expected_prompt


@pytest.mark.parametrize(
    "checkpoint, expected_tokenizer, expected_collator",
    [
        (
            "deepseek-ai/deepseek-coder-1.3b-base",
            LlamaTokenizerFast,
            DataCollatorWithPadding,
        ),
        ("Qwen/Qwen2.5-Coder-14B", Qwen2TokenizerFast, DataCollatorWithPadding),
    ],
)
def test_set_tokenizer(checkpoint, expected_tokenizer, expected_collator):
    tokenizer, data_collator = set_tokenizer(checkpoint)
    assert tokenizer.__class__ == expected_tokenizer
    assert data_collator.__class__ == expected_collator


@pytest.fixture
def expected_data():
    expected = {
    "input_ids": [
        [
            32013, 185, 655, 6147, 1895, 254, 2974, 4494, 515, 6479, 878, 25, 506, 7,
            16, 650, 506, 7, 2022, 77, 650, 506, 7, 77, 650, 506, 7, 77, 2022, 77,
            650, 185, 3462, 506, 7, 77, 8494, 207, 17, 650, 506, 7, 77, 8494, 207,
            18, 650, 21807, 13, 1306, 967, 254, 3495, 372, 254, 5933, 185, 1044,
            2557, 506, 761, 13954, 4976, 13, 185, 655, 10587, 25, 473, 16194, 1659,
            18610, 3214, 185, 185, 64, 11, 353, 405, 3579, 7, 569, 11, 2773, 3433,
            7818, 4683, 185, 75, 11, 263, 11, 259, 405, 3579, 7, 569, 11, 2773,
            3433, 7818, 4683, 185, 185, 1551, 1273, 83, 7, 84, 11, 353, 11, 245,
            11, 1302, 1772, 185, 184, 7661, 405, 334, 85, 9, 85, 12, 84, 9, 84,
            9402, 7, 17, 9, 64, 8, 185, 2944, 3853, 1938, 1302, 25, 185, 184, 3404,
            334, 4215, 7, 84, 9, 84, 10, 17, 9, 64, 9, 5977, 6906, 84, 9402, 64,
            185, 3404, 334, 85, 12, 84, 9402, 64, 945, 334, 5977, 12, 7661, 9402,
            85, 185, 185, 1551, 8711, 7, 64, 11, 353, 11, 284, 11, 263, 11, 259,
            1772, 185, 2944, 353, 14443, 259, 409, 207, 17, 9, 64, 9, 67, 14443,
            259, 9, 86, 25, 185, 184, 3404, 1273, 83, 7, 15, 11, 353, 11, 245, 11,
            284, 8, 185, 184, 6747, 405, 1273, 83, 7, 86, 11, 353, 11, 245, 11,
            284, 12, 67, 8, 185, 184, 31308, 405, 18610, 3214, 7, 64, 9, 67, 945,
            259, 9, 86, 14, 17, 8, 185, 2944, 11320, 1938, 353, 25, 185, 184, 184,
            7246, 845, 405, 334, 85, 9, 85, 12, 86, 9, 86, 14, 17, 9402, 64, 185,
            184, 184, 7613, 405, 334, 17, 9, 85, 12, 86, 9402, 64, 945, 334, 67,
            12, 7246, 845, 9402, 85, 185, 18052, 25, 185, 184, 184, 7613, 405, 334,
            17, 9, 31308, 12, 86, 9402, 64, 185, 3404, 1321, 945, 1164, 185, 185,
            4128, 7, 69, 6, 90, 9628, 312, 7, 64, 11, 353, 11, 284, 11, 263, 11,
            259, 1772, 13, 23, 69, 92, 2462
        ],
        [
            32013, 3154, 16194, 1659, 572, 185, 64, 11, 25244, 405, 3579, 7, 569,
            11, 2773, 3433, 7818, 4683, 185, 75, 11, 263, 11, 353, 67, 405, 3579,
            7, 569, 11, 2773, 3433, 7818, 4683, 185, 351, 25244, 14443, 353, 67,
            409, 18610, 3214, 7, 17, 572, 245, 572, 263, 8, 14443, 353, 67, 25,
            185, 315, 562, 25244, 9220, 207, 17, 889, 334, 17, 572, 245, 8, 17237,
            284, 25, 185, 436, 274, 82, 405, 18610, 3214, 7, 17, 572, 284, 889,
            245, 8, 185, 315, 1969, 25, 185, 436, 274, 82, 405, 25244, 889, 245,
            945, 334, 75, 567, 25244, 9220, 207, 17, 889, 334, 17, 572, 245, 1435,
            889, 25244, 185, 7736, 25, 185, 315, 252, 16, 405, 334, 9732, 9220,
            207, 17, 567, 353, 67, 9220, 207, 17, 8, 889, 334, 17, 572, 245, 8,
            185, 315, 562, 252, 16, 17237, 334, 75, 567, 263, 1772, 185, 436, 274,
            82, 405, 334, 4215, 7, 19, 572, 334, 17434, 9220, 207, 17, 8, 4536, 23,
            572, 245, 572, 334, 75, 567, 263, 1435, 567, 207, 17, 572, 353, 67, 8,
            889, 334, 17, 572, 245, 8, 185, 315, 1969, 25, 185, 436, 274, 82, 405,
            334, 9732, 567, 353, 67, 8, 889, 245, 945, 334, 75, 567, 263, 567, 252,
            16, 8, 889, 25244, 185, 315, 353, 16, 405, 18610, 3214, 5930, 17, 572,
            245, 572, 263, 945, 353, 67, 9220, 207, 17, 8, 889, 207, 17, 8, 185,
            315, 562, 353, 16, 14443, 25244, 25, 185, 436, 274, 82, 405, 274, 82,
            945, 353, 16, 889, 245, 945, 334, 85, 16, 567, 353, 67, 8, 889, 245,
            185, 315, 1969, 25, 185, 436, 252, 16, 405, 263, 567, 334, 9732, 9220,
            207, 17, 567, 353, 67, 9220, 207, 17, 8, 889, 334, 17, 572, 245, 8,
            567, 334, 9732, 9220, 207, 17, 8, 889, 334, 17, 572, 245, 8, 185, 436,
            274, 82, 405, 274, 82, 945, 25244, 889, 245, 945, 334, 9732, 567, 353,
            67, 8, 889, 245, 945, 252, 16, 889, 25244, 185, 4128, 1497, 13027, 16,
            17, 69, 6, 3018, 274, 82, 8, 185
        ]
    ],
    "attention_mask": [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                           , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    "labels": [0, 0],
}

    return Dataset.from_dict(expected)


def test_tokenize_data(df, expected_data, tokenizer):
    data_to_test = Dataset.from_pandas(df.iloc[:2])

    got = data_to_test.map(
        lambda x: tokenize_data(x, tokenizer, label2id), batched=True, remove_columns=data_to_test.column_names
    )

    assert got['input_ids'] == expected_data['input_ids'] 
    assert got['attention_mask'] == expected_data['attention_mask'] 
    assert got['labels'] == expected_data['labels'] 
