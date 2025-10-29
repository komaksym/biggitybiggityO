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
    return BASE_LOCATION.parent / "dummy_data/dummy_target_data.csv"