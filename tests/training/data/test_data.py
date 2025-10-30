import great_expectations as gx
import pandas as pd
import pytest
from pathlib import Path
from src.training.code.scripts.data import find_paths, generate_prompt

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
    suite.add_expectation(gx.expectations.ExpectTableColumnsToMatchOrderedList(column_list=column_list))
    complexities = ["O(1)", "O(logn)", "O(n)", "O(nlogn)", "O(n ^ 2)", "O(n ^ 3)", "np"]
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeInSet(column="complexity", value_set=complexities)
    )
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="code"))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="code"))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="complexity"))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeOfType(column="code", type_="str"))
    suite.add_expectation(gx.expectations.ExpectColumnValuesToBeOfType(column="complexity", type_="str"))

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
    assert got['code'].iloc[0] == expected_prompt
