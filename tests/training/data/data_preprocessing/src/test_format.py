from data.preprocessing_scripts.scripts.format import format_data
from data.preprocessing_scripts.scripts.utils import save_data
import pytest
import pandas as pd


@pytest.fixture(scope="package")
def dummy_dataset(tmp_path_factory) -> pd.DataFrame:
    """Create a temp dataset"""
    tmp_data = pd.DataFrame({"code": ["class Solution(object):\n    def findEvenNumbers(self, digits):\n        k = 3\n        def backtracking(curr, cnt, result): \n# Testing testing 123\n\n            if len(curr) == k:\n                result.append(reduce(lambda x, y: x*10+y, curr))\n                return\n            for i, c in enumerate(cnt):\n                if c == 0 or (not curr and i == 0) or (len(curr) == k-1 and i%2 != 0):\n                    continue\n                cnt[i] -= 1\n                curr.append(i)\n                backtracking(curr, cnt, result)\n                curr.pop()\n                cnt[i] += 1\n\n        cnt = [0]*10\n        for d in digits:\n            cnt[d] += 1\n        result = []\n        backtracking([], cnt, result)\n        return result", "class Solution2(object):\n    def findEvenNumbers(self, digits):\n\n\n\n\n\n\n\n        result, cnt = [], collections.Counter(digits)\n        for i in range(1, 10):\n            for j in range(10):\n                for k in range(0, 10, 2):\n                    if cnt[i] > 0 and cnt[j] > (j == i) and cnt[k] > (k == i) + (k == j):\n                        result.append(i*100 + j*10 + k)\n        return result", "class Solution3(object):\n    def findEvenNumbers(self, digits):\n        k = 3\n        \n        def backtracking(curr, dummy, result):\n            if len(curr) == k:\n                result.append(reduce(lambda x, y: x*10+y, curr))\n                return\n            node = dummy.right\n            while node:\n                if (not curr and node.val[0] == 0) or (len(curr) == k-1 and node.val[0]%2 != 0):\n                    node = node.right\n                    continue\n                node.val[1] -= 1\n                if node.val[1] == 0:\n                    if node.left:\n                        node.left.right = node.right\n                    if node.right:\n                        node.right.left = node.left\n                curr.append(node.val[0])\n                backtracking(curr, dummy, result)\n                curr.pop()\n                if node.val[1] == 0:\n                    if node.left:\n                        node.left.right = node\n                    if node.right:\n                        node.right.left = node\n                node.val[1] += 1\n                node = node.right\n\n        prev = dummy = Node()\n        for digit, cnt in sorted(map(list, iter(collections.Counter(digits).items()))):\n            prev.right = Node(val=[digit, cnt], left=prev)\n            prev = prev.right\n        result = []\n        backtracking([], dummy, result)\n        return result"],
                             "complexity": ['O(n)', '# Time:  O(n), n is 10^3', '# Time:  O(1) ~ O(n), n is 10^3']})
    file_path = tmp_path_factory.mktemp("dummy_data") / "df.csv"
    save_data(tmp_data, file_path)
    return tmp_data
    


@pytest.fixture
def expected_formatted_data() -> pd.DataFrame:
    """Expected data post-format"""
    return pd.DataFrame({
        "code": [
            "class Solution(object):\n    def findEvenNumbers(self, digits):\n        k = 3\n        def backtracking(curr, cnt, result):\n\n            if len(curr) == k:\n                result.append(reduce(lambda x, y: x*10+y, curr))\n                return\n            for i, c in enumerate(cnt):\n                if c == 0 or (not curr and i == 0) or (len(curr) == k-1 and i%2 != 0):\n                    continue\n                cnt[i] -= 1\n                curr.append(i)\n                backtracking(curr, cnt, result)\n                curr.pop()\n                cnt[i] += 1\n\n        cnt = [0]*10\n        for d in digits:\n            cnt[d] += 1\n        result = []\n        backtracking([], cnt, result)\n        return result"
        ],
        "complexity": ["O(n)"],
    })


def test_format_data(dummy_dataset, expected_formatted_data) -> None:
    got: pd.DataFrame = format_data(dummy_dataset)

    assert got.equals(expected_formatted_data)