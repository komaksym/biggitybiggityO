from pathlib import Path

import pandas as pd
import pytest

from ..utils import get_file_extension, read_data, save_data

BASE_LOCATION: Path = Path(__file__).parent


@pytest.fixture
def dummy_source_path() -> Path:
    """Dummy file source path."""
    return BASE_LOCATION / "dummy_data/dummy_src_data.csv"


@pytest.fixture
def expected_file_extension() -> str:
    """Dummy expected file extension."""
    return "csv"


def test_get_file_extension(dummy_source_path: Path, expected_file_extension: str) -> None:
    """Test the get_file_extension function."""
    got: str = get_file_extension(dummy_source_path)

    assert got == expected_file_extension


@pytest.fixture
def expected_read_data() -> pd.DataFrame:
    """Dummy expected data that is read"""
    return pd.DataFrame(
        {
            "code": [
                "class Solution(object):\n    def findEvenNumbers(self, digits):\n        k = 3\n        def backtracking(curr, cnt, result):\n            if len(curr) == k:\n                result.append(reduce(lambda x, y: x*10+y, curr))\n                return\n            for i, c in enumerate(cnt):\n                if c == 0 or (not curr and i == 0) or (len(curr) == k-1 and i%2 != 0):\n                    continue\n                cnt[i] -= 1\n                curr.append(i)\n                backtracking(curr, cnt, result)\n                curr.pop()\n                cnt[i] += 1\n\n        cnt = [0]*10\n        for d in digits:\n            cnt[d] += 1\n        result = []\n        backtracking([], cnt, result)\n        return result\n\n",
                "class Solution2(object):\n    def findEvenNumbers(self, digits):\n        result, cnt = [], collections.Counter(digits)\n        for i in range(1, 10):\n            for j in range(10):\n                for k in range(0, 10, 2):\n                    if cnt[i] > 0 and cnt[j] > (j == i) and cnt[k] > (k == i) + (k == j):\n                        result.append(i*100 + j*10 + k)\n        return result\n\n",
                "class Solution3(object):\n    def findEvenNumbers(self, digits):\n        k = 3\n        \n        def backtracking(curr, dummy, result):\n            if len(curr) == k:\n                result.append(reduce(lambda x, y: x*10+y, curr))\n                return\n            node = dummy.right\n            while node:\n                if (not curr and node.val[0] == 0) or (len(curr) == k-1 and node.val[0]%2 != 0):\n                    node = node.right\n                    continue\n                node.val[1] -= 1\n                if node.val[1] == 0:\n                    if node.left:\n                        node.left.right = node.right\n                    if node.right:\n                        node.right.left = node.left\n                curr.append(node.val[0])\n                backtracking(curr, dummy, result)\n                curr.pop()\n                if node.val[1] == 0:\n                    if node.left:\n                        node.left.right = node\n                    if node.right:\n                        node.right.left = node\n                node.val[1] += 1\n                node = node.right\n\n        prev = dummy = Node()\n        for digit, cnt in sorted(map(list, iter(collections.Counter(digits).items()))):\n            prev.right = Node(val=[digit, cnt], left=prev)\n            prev = prev.right\n        result = []\n        backtracking([], dummy, result)\n        return result\n\n",
            ],
            "complexity": [
                "# Time:  O(1) ~ O(n), n is 10^3",
                "# Time:  O(n), n is 10^3",
                "# Time:  O(1) ~ O(n), n is 10^3",
            ],
        }
    )


def test_read_data(dummy_source_path: Path, expected_read_data: pd.DataFrame) -> None:
    """Test if read data works correctly."""
    got: pd.DataFrame = read_data(dummy_source_path)

    assert got.equals(expected_read_data)


@pytest.fixture
def dummy_target_path() -> Path:
    return BASE_LOCATION / "dummy_data/dummy_target_data.csv"


def test_save_data(dummy_source_path, dummy_target_path) -> None:
    """Test if save_data works correctly and saves a file."""
    data: pd.DataFrame = read_data(dummy_source_path)

    save_data(data, dummy_target_path)

    assert dummy_target_path.exists()