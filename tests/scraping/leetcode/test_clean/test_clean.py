import re
from pathlib import Path
from typing import Any

import pytest

from src.scraping.leetcode_solutions.src.clean import FileCleaner


@pytest.fixture
def filter_pattern() -> re.Pattern[str]:
    return re.compile(
        r"(#.*?$)|(\"{3}.*?\"{3})|('{3}.*?'{3})",
        flags=re.DOTALL | re.IGNORECASE | re.MULTILINE,
    )


@pytest.fixture
def expected_parsed_data() -> dict[str, list[str]]:
    return {
        "code": [
            "class Solution(object):\n\n    def __init__(self, root):\n        self.__tree = [root]\n        for i in self.__tree:\n            if i.left:\n                self.__tree.append(i.left)\n            if i.right:\n                self.__tree.append(i.right)        \n\n    def insert(self, v):\n        n = len(self.__tree)\n        self.__tree.append(TreeNode(v))\n        if n % 2:\n            self.__tree[(n-1)//2].left = self.__tree[-1]\n        else:\n            self.__tree[(n-1)//2].right = self.__tree[-1]\n        return self.__tree[(n-1)//2].val\n\n    def get_root(self):\n        return self.__tree[0]\n\n\n",
            'class Solution(object):\n    def splitLoopedString(self, strs):\n        tmp = []\n        for s in strs:\n            tmp += max(s, s[::-1])\n        s = "".join(tmp)\n\n        result, st = "a", 0\n        for i in range(len(strs)):\n            body = "".join([s[st + len(strs[i]):], s[0:st]])\n            for p in strs[i], strs[i][::-1]:\n                for j in range(len(strs[i])):\n                    if p[j] >= result[0]:\n                        result = max(result, "".join([p[j:], body, p[:j]]))\n            st += len(strs[i])\n        return result\n',
            "class Solution(object):\n    def rearrangeBarcodes(self, barcodes):\n        k = 2\n        cnts = collections.Counter(barcodes)\n        bucket_cnt = max(cnts.values())\n        result = [0]*len(barcodes)\n        i = (len(barcodes)-1)%k\n        for c in itertools.chain((c for c, v in cnts.items() if v == bucket_cnt), (c for c, v in cnts.items() if v != bucket_cnt)):\n            for _ in range(cnts[c]):\n                result[i] = c\n                i += k\n                if i >= len(result):\n                    i = (i-1)%k\n        return result\n\nimport collections\n\n",
            "class Solution2(object):\n    def rearrangeBarcodes(self, barcodes):\n        cnts = collections.Counter(barcodes)\n        sorted_cnts = [[v, k] for k, v in cnts.items()]\n        sorted_cnts.sort(reverse=True)\n\n        i = 0\n        for v, k in sorted_cnts:\n            for _ in range(v):\n                barcodes[i] = k\n                i += 2\n                if i >= len(barcodes):\n                    i = 1\n        return barcodes",
            "class Solution(object):\n    def __init__(self):\n        self.__root = None\n\n\n    def book(self, start, end):\n        if self.__root is None:\n            self.__root = Node(start, end)\n            return True\n        return self.root.insert(Node(start, end))\n\n",
            "class Solution2(object):\n\n    def __init__(self):\n        self.__calendar = []\n\n\n    def book(self, start, end):\n        for i, j in self.__calendar:\n            if start < j and end > i:\n                return False\n        self.__calendar.append((start, end))\n        return True\n\n\n",
        ],
        "label": [
            "# Time:  ctor:     O(n)\n#        insert:   O(1)\n#        get_root: O(1)",
            "# Time:  O(n^2)",
            "# Time:  O(n), k is the number of distinct barcodes",
            "# Time:  O(n), k is the number of distinct barcodes",
            "# Time:  O(nlogn) on average, O(n^2) on worst case",
            "# Time:  O(n^2)",
        ],
    }


@pytest.fixture
def expected_corrupted_data() -> list[Any]:
    return []


def test_clean_files(
    expected_raw_data, expected_parsed_data, expected_corrupted_data, filter_pattern
) -> None:
    parsed_data: dict[str, list[str]]
    corrupted_data: list[Path | str]

    parsed_data, corrupted_data = FileCleaner().clean(
        **expected_raw_data, regex_pattern=filter_pattern
    )

    assert (parsed_data == expected_parsed_data) and (corrupted_data == expected_corrupted_data)
