import pytest
from ..split import DatasetSplitter
from ..utils import read_data
from pathlib import Path
import pandas as pd

BASE_LOCATION: Path = Path(__file__).parent


@pytest.fixture
def dummy_source_path() -> Path:
    return BASE_LOCATION / "dummy_data/dummy_src_data.csv"


@pytest.fixture
def dummy_train_set_path() -> Path:
    return BASE_LOCATION / "dummy_data/dummy_train_set.csv"


@pytest.fixture
def dummy_test_set_path() -> Path:
    return BASE_LOCATION / "dummy_data/dummy_test_set.csv"


@pytest.fixture
def expected_split_datasets() -> tuple[pd.DataFrame, pd.DataFrame]:
    train_set = pd.DataFrame(
        {
            "code": [
                "class Solution2(object):\n    def findEvenNumbers(self, digits):\n        result, cnt = [], collections.Counter(digits)\n        for i in range(1, 10):\n            for j in range(10):\n                for k in range(0, 10, 2):\n                    if cnt[i] > 0 and cnt[j] > (j == i) and cnt[k] > (k == i) + (k == j):\n                        result.append(i*100 + j*10 + k)\n        return result\n\n",
                "class Solution3(object):\n    def findEvenNumbers(self, digits):\n        k = 3\n        \n        def backtracking(curr, dummy, result):\n            if len(curr) == k:\n                result.append(reduce(lambda x, y: x*10+y, curr))\n                return\n            node = dummy.right\n            while node:\n                if (not curr and node.val[0] == 0) or (len(curr) == k-1 and node.val[0]%2 != 0):\n                    node = node.right\n                    continue\n                node.val[1] -= 1\n                if node.val[1] == 0:\n                    if node.left:\n                        node.left.right = node.right\n                    if node.right:\n                        node.right.left = node.left\n                curr.append(node.val[0])\n                backtracking(curr, dummy, result)\n                curr.pop()\n                if node.val[1] == 0:\n                    if node.left:\n                        node.left.right = node\n                    if node.right:\n                        node.right.left = node\n                node.val[1] += 1\n                node = node.right\n\n        prev = dummy = Node()\n        for digit, cnt in sorted(map(list, iter(collections.Counter(digits).items()))):\n            prev.right = Node(val=[digit, cnt], left=prev)\n            prev = prev.right\n        result = []\n        backtracking([], dummy, result)\n        return result\n\n",
            ],
            "complexity": ["# Time:  O(n), n is 10^3", "# Time:  O(1) ~ O(n), n is 10^3"],
        }
    )
    test_set = pd.DataFrame(
        {
            "code": [
                "class Solution(object):\n    def findEvenNumbers(self, digits):\n        k = 3\n        def backtracking(curr, cnt, result):\n            if len(curr) == k:\n                result.append(reduce(lambda x, y: x*10+y, curr))\n                return\n            for i, c in enumerate(cnt):\n                if c == 0 or (not curr and i == 0) or (len(curr) == k-1 and i%2 != 0):\n                    continue\n                cnt[i] -= 1\n                curr.append(i)\n                backtracking(curr, cnt, result)\n                curr.pop()\n                cnt[i] += 1\n\n        cnt = [0]*10\n        for d in digits:\n            cnt[d] += 1\n        result = []\n        backtracking([], cnt, result)\n        return result\n\n",
            ],
            "complexity": ["# Time:  O(1) ~ O(n), n is 10^3"],
        }
    )

    return train_set, test_set


def test_DatasetSplitter(
    dummy_source_path: Path,
    dummy_train_set_path: Path,
    dummy_test_set_path: Path,
    expected_split_datasets: tuple[pd.DataFrame, pd.DataFrame],
) -> None:
    """Test DatasetSplitter and check if it splits correctly into train/test sets."""

    splitter = DatasetSplitter(dummy_source_path, dummy_train_set_path, dummy_test_set_path)
    splitter.run()

    # Test whether files were successfully created.
    assert dummy_train_set_path.exists() and dummy_test_set_path.exists()

    got_train_set: pd.DataFrame = read_data(dummy_train_set_path)
    got_test_set: pd.DataFrame = read_data(dummy_test_set_path)

    expected_train_set, expected_test_set = expected_split_datasets

    # Test whether files' contents equal expected
    assert got_train_set.equals(expected_train_set) and got_test_set.equals(expected_test_set)
