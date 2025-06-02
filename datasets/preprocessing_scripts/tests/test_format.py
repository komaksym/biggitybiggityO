from ..format import format_data
from ..utils import read_data
from pathlib import Path
import pytest
import pandas as pd


BASE_LOCATION: Path = Path(__file__).parent


@pytest.fixture
def dummy_source_path() -> Path:
    return BASE_LOCATION / "dummy_data/dummy_src_data.csv"


@pytest.fixture
def expected_formatted_data():
    return pd.DataFrame({
        "code": [
            "class Solution(object):\n    def findEvenNumbers(self, digits):\n        k = 3\n        def backtracking(curr, cnt, result):\n\n            if len(curr) == k:\n                result.append(reduce(lambda x, y: x*10+y, curr))\n                return\n            for i, c in enumerate(cnt):\n                if c == 0 or (not curr and i == 0) or (len(curr) == k-1 and i%2 != 0):\n                    continue\n                cnt[i] -= 1\n                curr.append(i)\n                backtracking(curr, cnt, result)\n                curr.pop()\n                cnt[i] += 1\n\n        cnt = [0]*10\n        for d in digits:\n            cnt[d] += 1\n        result = []\n        backtracking([], cnt, result)\n        return result"
        ],
        "complexity": ["O(n)"],
    })


def test_format_data(dummy_source_path, expected_formatted_data):
    got = format_data(read_data(dummy_source_path))

    assert got.equals(expected_formatted_data)