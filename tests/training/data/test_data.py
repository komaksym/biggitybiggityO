import great_expectations as gx
import pandas as pd
import pytest
from pathlib import Path
from pprint import pprint

BASE_PATH = Path(__file__).parent

@pytest.fixture(scope="module")
def df_path():
    return BASE_PATH.parents[2] / "datasets/data/merges/codecomplex+neetcode+leetcode_clean/full_no_exponential+factorial/full_no_exponential+factorial.csv"

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
    suite.add_expectation(
        gx.expectations.ExpectTableColumnsToMatchOrderedList(column_list=column_list)
    )
    complexities = ["O(1)", "O(logn)", "O(n)", "O(nlogn)", "O(n ^ 2)", "O(n ^ 3)", "np"]
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeInSet(column="complexity", value_set=complexities)
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeUnique(column="code")
    )
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="code")
    )
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
    assert validation_results['success']

    