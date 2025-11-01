"""
This file is automatically imported to every test in the package
so we add common fixtures here to not create them in every module
or import to every module the same fixture.
"""
import pytest
from pathlib import Path


BASE_LOCATION: Path = Path(__file__).parent


@pytest.fixture
def dummy_source_file_path() -> Path:
    """Dummy file source path."""
    return BASE_LOCATION.parent / "dummy_data/dummy_src_data.csv"



@pytest.fixture
def dummy_target_file_path() -> Path:
    """Return Path to the dummy target CSV file used by tests.

    The file is located in the sibling `dummy_data` directory and provides
    a small target dataset used by preprocessing unit tests.
    """

    return BASE_LOCATION.parent / "dummy_data/dummy_target_data.csv"