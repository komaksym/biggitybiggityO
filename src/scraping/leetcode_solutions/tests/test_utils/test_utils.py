from pathlib import Path

import pytest

from ...src.utils import MyDict, search_files

BASE_LOCATION: Path = Path(__file__).parent


@pytest.fixture
def src_files_path() -> Path:
    """Returns path to mock source files."""
    return BASE_LOCATION / "mock_files/"


def test_search_files(src_files_path, expected_raw_data) -> None:
    """Tests search files"""
    got: MyDict = search_files(src_files_path)

    assert got == expected_raw_data
