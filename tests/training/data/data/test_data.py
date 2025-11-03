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
    """Return Path to the full CSV dataset used by the tests.

    The path points to the merged 'full_no_exponential+factorial' CSV file
    inside the repository's data directory.
    """
    return (
        BASE_LOCATION.parents[3]
        / "data/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial/full_no_exponential+factorial.csv"
    )


@pytest.fixture(scope="module")
def df(df_path):
    """Load the CSV at `df_path` and return a pandas DataFrame.

    This fixture provides the dataset used by multiple tests.
    """

    return pd.read_csv(df_path)


@pytest.fixture(scope="module")
def tokenizer_path():
    """Return a Path to the pretrained tokenizer directory used in tests.

    The directory contains the tokenizer files for the 'deepseek-coder-1.3b-base' model.
    """

    return "deepseek-ai/deepseek-coder-1.3b-base"


@pytest.fixture(scope="module")
def tokenizer(tokenizer_path):
    """Load and return an AutoTokenizer from the provided `tokenizer_path`.

    The tokenizer is used for tokenization-related tests in this module.
    """

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
            "train": BASE_LOCATION.parents[3]
            / "data/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial"
            / "train_set.csv",
            "eval": BASE_LOCATION.parents[3]
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
    """Expected output for testing generate_prompt function"""

    return "\n            Classify the code snippet into: O(1), O(logn), O(n), O(nlogn),\n              O(n ^ 2), O(n ^ 3), np. And return the answer as the corresponding\n                big O time complexity label.\n            Code: from math import sqrt\n\na, v = map(int, input().split())\nl, d, w = map(int, input().split())\n\ndef findt(u, v, a, dist):\n\tfront = (v*v-u*u)/(2*a)\n\tif front > dist:\n\t\treturn (sqrt(u*u+2*a*dist)-u)/a\n\treturn (v-u)/a + (dist-front)/v\n\ndef solve(a, v, l, d, w):\n\tif v <= w or 2*a*d <= w*w:\n\t\treturn findt(0, v, a, l)\n\tafter = findt(w, v, a, l-d)\n\tpeak = sqrt(a*d + w*w/2)\n\tif peak > v:\n\t\ttravel = (v*v-w*w/2)/a\n\t\tbefore = (2*v-w)/a + (d-travel)/v\n\telse:\n\t\tbefore = (2*peak-w)/a\n\treturn before + after\n\nprint(f'{solve(a, v, l, d, w):.8f}')"


def test_generate_prompt(df, expected_prompt):
    """Verify `generate_prompt` wraps a code sample in the expected instruction template.

    The test takes the first row from the dataset and ensures the generated
    prompt matches the long multi-line expected string.
    """

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
    """Assert that `set_tokenizer` returns the correct tokenizer and collator types.

    Parametrized over known checkpoints to ensure the function selects the
    appropriate fast tokenizer implementation and a padding collator.
    """

    tokenizer, data_collator = set_tokenizer(checkpoint)

    assert isinstance(tokenizer, expected_tokenizer)
    assert isinstance(data_collator, expected_collator)


@pytest.fixture
def expected_data():
    """Return a small expected tokenized dataset as a Hugging Face Dataset.

    The returned Dataset contains `input_ids`, `attention_mask`, and `labels`
    for asserting correctness of `tokenize_data` on a two-row sample.
    """

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
    """Tokenize the first two rows of the dataframe and compare with expected.

    Uses the provided `tokenizer` and `label2id` mapping to produce
    `input_ids`, `attention_mask`, and `labels` and asserts exact equality.
    """

    data_to_test = Dataset.from_pandas(df.iloc[:2])

    got = data_to_test.map(
        lambda x: tokenize_data(x, tokenizer, label2id), batched=True, remove_columns=data_to_test.column_names
    )

    assert got['input_ids'] == expected_data['input_ids'] 
    assert got['attention_mask'] == expected_data['attention_mask'] 
    assert got['labels'] == expected_data['labels'] 


@pytest.fixture
def expected_tokenized_data():
    """Return expected tokenized train and eval sets as Hugging Face Datasets.

    These fixtures represent the expected outputs of the full data pipeline's
    tokenization step for a small mocked train/eval split.
    """

    expected_train_set = {
        "input_ids": [[32013, 185, 655, 6147, 1895, 254, 2974, 4494, 515, 6479, 878, 25, 506, 7, 16, 650, 506, 7, 2022, 77, 650, 506, 7, 77, 650, 506, 7, 77, 2022, 77, 650, 185, 3462, 506, 7, 77, 8494, 207, 17, 650, 506, 7, 77, 8494, 207, 18, 650, 21807, 13, 1306, 967, 254, 3495, 372, 254, 5933, 185, 1044, 2557, 506, 761, 13954, 4976, 13, 185, 655, 10587, 25, 1659, 19060, 11, 10925, 11, 12156, 185, 185, 3584, 405, 19060, 13, 15282, 6860, 7, 378, 13, 1187, 7, 15, 11, 378, 13, 69, 10270, 7, 15, 628, 292, 62, 3017, 14462, 1187, 1027, 185, 185, 1551, 1272, 10942, 185, 315, 291, 11, 273, 11, 528, 405, 3579, 7, 569, 11, 2773, 3433, 7818, 822, 2189, 185, 185, 315, 286, 405, 821, 2493, 7, 4008, 7, 569, 11, 2773, 3433, 7818, 822, 2189, 2189, 10, 821, 9986, 1195, 10, 7799, 17359, 327, 1070, 279, 3160, 7, 77, 6651, 185, 185, 315, 353, 405, 821, 2493, 7, 4008, 7, 569, 11, 2773, 3433, 7818, 822, 2189, 2189, 327, 1070, 279, 3160, 7, 77, 12, 16, 6651, 185, 315, 353, 13, 6880, 7, 821, 9986, 1195, 10, 7799, 17359, 572, 273, 2189, 185, 185, 315, 8711, 7, 77, 11, 273, 11, 528, 11, 286, 11, 353, 8, 185, 185, 1551, 8711, 7, 77, 11, 273, 11, 528, 11, 286, 11, 353, 1772, 185, 315, 562, 528, 3018, 207, 17, 25, 185, 436, 274, 82, 405, 17436, 16, 440, 572, 273, 185, 436, 327, 1070, 279, 3160, 7, 77, 1772, 185, 655, 3628, 7, 531, 8, 185, 436, 967, 185, 185, 315, 263, 79, 405, 821, 821, 15, 60, 572, 334, 76, 10, 16, 8, 327, 1070, 279, 3160, 7, 77, 10, 16, 6651, 185, 185, 315, 291, 530, 405, 821, 821, 15, 60, 572, 334, 76, 10, 16, 8, 327, 207, 1070, 279, 3160, 7, 77, 10, 16, 6651, 185, 185, 315, 327, 1070, 279, 3160, 7, 17, 11, 528, 4536, 16, 11, 207, 17, 1772, 185, 185, 436, 327, 460, 279, 3160, 7, 77, 1772, 185, 655, 327, 521, 279, 3160, 7, 76, 1772, 185, 1044, 284, 1412, 17, 572, 286, 58, 72, 6872, 73, 12, 16, 60, 945, 263, 79, 58, 72, 6872, 73, 12, 16, 60, 185, 1044, 427, 1412, 17, 572, 286, 58, 72, 6872, 73, 60, 16838, 263, 79, 58, 72, 6872, 73, 10, 16, 60, 185, 1044, 2631, 1412, 17, 572, 353, 58, 72, 12, 16, 6872, 73, 60, 945, 263, 79, 58, 72, 12, 16, 6872, 73, 60, 185, 1044, 263, 1412, 17, 572, 353, 58, 72, 6872, 73, 60, 16838, 263, 79, 58, 72, 10, 16, 6872, 73, 60, 185, 185, 1044, 3589, 405, 1344, 7, 75, 11, 427, 8, 185, 1044, 2427, 405, 1344, 7, 84, 11, 263, 8, 185, 185, 1044, 291, 530, 58, 72, 6872, 73, 60, 405, 1344, 7, 2107, 11, 2427, 8, 185, 185, 436, 263, 79, 11, 291, 530, 405, 291, 530, 11, 263, 79, 185, 185, 315, 327, 284, 279, 263, 79, 17052, 12, 16, 5859, 185, 436, 3628, 1195, 19736]],
        "attention_mask": [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        "labels": [5]
    }

    expected_eval_set = {
        "input_ids": [[32013, 185, 655, 6147, 1895, 254, 2974, 4494, 515, 6479, 878, 25, 506, 7, 16, 650, 506, 7, 2022, 77, 650, 506, 7, 77, 650, 506, 7, 77, 2022, 77, 650, 185, 3462, 506, 7, 77, 8494, 207, 17, 650, 506, 7, 77, 8494, 207, 18, 650, 21807, 13, 1306, 967, 254, 3495, 372, 254, 5933, 185, 1044, 2557, 506, 761, 13954, 4976, 13, 185, 655, 10587, 25, 757, 324, 3548, 18, 7, 4534, 1772, 185, 185, 315, 972, 5576, 2995, 14372, 1180, 1772, 185, 436, 1781, 13, 8710, 405, 9635, 185, 185, 315, 972, 7886, 7, 1180, 11, 1371, 1772, 185, 436, 562, 1781, 13, 8710, 25, 185, 655, 1642, 62, 1513, 405, 1344, 7, 87, 11, 1781, 13, 8710, 13857, 16, 6872, 15, 5589, 185, 655, 1781, 13, 8710, 13, 6880, 5930, 5824, 62, 1513, 11, 1371, 1435, 185, 436, 1969, 25, 185, 655, 1781, 13, 8710, 13, 6880, 5930, 87, 11, 1371, 1435, 185, 185, 315, 972, 2434, 7, 1180, 1772, 185, 436, 967, 1781, 13, 8710, 13, 9544, 822, 58, 16, 60, 185, 185, 315, 972, 1861, 7, 1180, 1772, 185, 436, 967, 1781, 13, 8710, 13857, 16, 6872, 16, 60, 185, 185, 315, 972, 748, 7729, 7, 1180, 1772, 185, 436, 967, 1781, 13, 8710, 13857, 16, 6872, 15, 60]],
        "attention_mask": [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        "labels": [0]
    }

    return Dataset.from_dict(expected_train_set), Dataset.from_dict(expected_eval_set)


def test_data_pipeline(dataset_paths, expected_data_paths, tokenizer, expected_tokenized_data):
    # Load paths up
    got_train_set_path, got_eval_set_path = find_paths(dataset_paths)

    assert got_train_set_path, got_eval_set_path == expected_data_paths

    # Read into pandas dataframes
    got_train_set = pd.read_csv(got_train_set_path)
    got_eval_set = pd.read_csv(got_eval_set_path)

    assert isinstance(got_train_set, pd.DataFrame)
    assert isinstance(got_eval_set, pd.DataFrame)

    # Apply instruction schema
    got_train_set = got_train_set.apply(generate_prompt, axis=1)
    got_eval_set = got_eval_set.apply(generate_prompt, axis=1)

    expected_train_set = pd.read_csv(BASE_LOCATION / "mock_expected_data/prompted_train_set.csv")
    expected_eval_set = pd.read_csv(BASE_LOCATION / "mock_expected_data/prompted_eval_set.csv")

    assert got_train_set.equals(expected_train_set)
    assert got_eval_set.equals(expected_eval_set)

    # Load as huggingface Datasets
    got_train_set = Dataset.from_pandas(got_train_set)
    got_eval_set = Dataset.from_pandas(got_eval_set)

    assert isinstance(got_train_set, Dataset)
    assert isinstance(got_eval_set, Dataset)

     # Tokenize train/eval sets
    got_train_set = got_train_set.map(
        lambda x: tokenize_data(x, tokenizer, label2id),
        batched=True,
        remove_columns=got_train_set.column_names,
    )

    got_eval_set = got_eval_set.map(
        lambda x: tokenize_data(x, tokenizer, label2id),
        batched=True,
        remove_columns=got_eval_set.column_names,
    )

    expected_train_set, expected_eval_set = expected_tokenized_data

    assert got_train_set['input_ids'][0] == expected_train_set['input_ids'][0]
    assert got_train_set['attention_mask'][0] == expected_train_set['attention_mask'][0]
    assert got_train_set['labels'][0] == expected_train_set['labels'][0]

    assert got_eval_set['input_ids'][0] == expected_eval_set['input_ids'][0]
    assert got_eval_set['attention_mask'][0] == expected_eval_set['attention_mask'][0]
    assert got_eval_set['labels'][0]== expected_eval_set['labels'][0]