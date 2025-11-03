from pathlib import Path
from typing import Any

import pytest

from src.scraping.leetcode_solutions.src.utils import MyDict, search_files
from src.scraping.leetcode_solutions.src.parse import FileParser

BASE_DIR: Path = Path(__file__).parent


@pytest.fixture
def mock_labels_txt() -> str:
    fp: Path = BASE_DIR / "mock_files/mock_labels.txt"

    with open(fp, "r") as f:
        return f.read()


@pytest.fixture
def expected_parsed_labels() -> list[str]:
    return [
        "n * m",
        "(logn)^2",
        "n * sqrt(n)",
        "n^(3/2)",
        "nlogn",
        "1",
        "max_n^2 + max_y * min(max_n, max_x)",
        "min(n, x)",
        "logn",
        "logn",
        "nlogn",
        "logn",
        "1",
    ]


def test_parse_labels(mock_labels_txt, expected_parsed_labels) -> None:
    got: list[str] = FileParser().parse_labels(mock_labels_txt)

    assert got == expected_parsed_labels


@pytest.fixture
def folder_path() -> Path:
    return BASE_DIR / "mock_files/"


@pytest.fixture
def expected_raw_data() -> MyDict:
    return {
        "file_paths": [
            Path(
                "/tests/scraping/leetcode/test_parse/mock_files/mock_files2/distant-barcodes.py"
            ),
            Path(
                "/tests/scraping/leetcode/test_parse/mock_files/mock_files2/my-calendar-i.py"
            ),
            Path(
                "/tests/scraping/leetcode/test_parse/mock_files/mock_files1/split-concatenated-strings.py"
            ),
            Path(
                "/tests/scraping/leetcode/test_parse/mock_files/mock_files1/complete-binary-tree-inserter.py"
            ),
        ],
        "files": [
            '# Time:  O(n), k is the number of distinct barcodes\n\nimport collections\nimport itertools\n\n\nclass Solution(object):\n    def rearrangeBarcodes(self, barcodes):\n        k = 2\n        cnts = collections.Counter(barcodes)\n        bucket_cnt = max(cnts.values())\n        result = [0]*len(barcodes)\n        i = (len(barcodes)-1)%k\n        for c in itertools.chain((c for c, v in cnts.items() if v == bucket_cnt), (c for c, v in cnts.items() if v != bucket_cnt)):\n            for _ in range(cnts[c]):\n                result[i] = c\n                i += k\n                if i >= len(result):\n                    i = (i-1)%k\n        return result\n\nimport collections\n\n\nclass Solution2(object):\n    def rearrangeBarcodes(self, barcodes):\n        cnts = collections.Counter(barcodes)\n        sorted_cnts = [[v, k] for k, v in cnts.items()]\n        sorted_cnts.sort(reverse=True)\n\n        i = 0\n        for v, k in sorted_cnts:\n            for _ in range(v):\n                barcodes[i] = k\n                i += 2\n                if i >= len(barcodes):\n                    i = 1\n        return barcodes\n',
            '# Time:  O(nlogn) on average, O(n^2) on worst case\n\nclass Node(object):\n    def __init__(self, start, end):\n        self.__start = start\n        self.__end = end\n        self.__left = None\n        self.__right = None\n\n\n    def insert(self, node):\n        if node.__start >= self.__end:\n            if not self.__right:\n                self.__right = node\n                return True\n            return self.__right.insert(node)\n        elif node.__end <= self.__start:\n            if not self.__left:\n                self.__left = node\n                return True\n            return self.__left.insert(node)\n        else:\n            return False\n\n\nclass Solution(object):\n    def __init__(self):\n        self.__root = None\n\n\n    def book(self, start, end):\n        if self.__root is None:\n            self.__root = Node(start, end)\n            return True\n        return self.root.insert(Node(start, end))\n\n\n# Time:  O(n^2)\nclass Solution2(object):\n\n    def __init__(self):\n        self.__calendar = []\n\n\n    def book(self, start, end):\n        for i, j in self.__calendar:\n            if start < j and end > i:\n                return False\n        self.__calendar.append((start, end))\n        return True\n\n\n\n',
            '# Time:  O(n^2)\n\nclass Solution(object):\n    def splitLoopedString(self, strs):\n        tmp = []\n        for s in strs:\n            tmp += max(s, s[::-1])\n        s = "".join(tmp)\n\n        result, st = "a", 0\n        for i in range(len(strs)):\n            body = "".join([s[st + len(strs[i]):], s[0:st]])\n            for p in strs[i], strs[i][::-1]:\n                for j in range(len(strs[i])):\n                    if p[j] >= result[0]:\n                        result = max(result, "".join([p[j:], body, p[:j]]))\n            st += len(strs[i])\n        return result\n\n',
            '# Time:  ctor:     O(n)\n#        insert:   O(1)\n#        get_root: O(1)\n\nclass TreeNode(object):\n    def __init__(self, x):\n        self.val = x\n        self.left = None\n        self.right = None\n\nclass Solution(object):\n\n    def __init__(self, root):\n        self.__tree = [root]\n        for i in self.__tree:\n            if i.left:\n                self.__tree.append(i.left)\n            if i.right:\n                self.__tree.append(i.right)        \n\n    def insert(self, v):\n        n = len(self.__tree)\n        self.__tree.append(TreeNode(v))\n        if n % 2:\n            self.__tree[(n-1)//2].left = self.__tree[-1]\n        else:\n            self.__tree[(n-1)//2].right = self.__tree[-1]\n        return self.__tree[(n-1)//2].val\n\n    def get_root(self):\n        return self.__tree[0]\n\n\n\n'
        ],
    }


def test_search_files(folder_path, expected_raw_data) -> None:
    got: MyDict = search_files(folder_path)

    assert got == expected_raw_data


@pytest.fixture
def expected_parsed_data() -> tuple[dict[str, list[str]], list[Path]]:
    return ({'code': ['\nimport collections\nimport itertools\n\n\nclass Solution(object):\n    def rearrangeBarcodes(self, barcodes):\n        k = 2\n        cnts = collections.Counter(barcodes)\n        bucket_cnt = max(cnts.values())\n        result = [0]*len(barcodes)\n        i = (len(barcodes)-1)%k\n        for c in itertools.chain((c for c, v in cnts.items() if v == bucket_cnt), (c for c, v in cnts.items() if v != bucket_cnt)):\n            for _ in range(cnts[c]):\n                result[i] = c\n                i += k\n                if i >= len(result):\n                    i = (i-1)%k\n        return result\n\nimport collections\n\n\nclass Solution2(object):\n    def rearrangeBarcodes(self, barcodes):\n        cnts = collections.Counter(barcodes)\n        sorted_cnts = [[v, k] for k, v in cnts.items()]\n        sorted_cnts.sort(reverse=True)\n\n        i = 0\n        for v, k in sorted_cnts:\n            for _ in range(v):\n                barcodes[i] = k\n                i += 2\n                if i >= len(barcodes):\n                    i = 1\n        return barcodes\n', '\nclass Solution(object):\n    def splitLoopedString(self, strs):\n        tmp = []\n        for s in strs:\n            tmp += max(s, s[::-1])\n        s = "".join(tmp)\n\n        result, st = "a", 0\n        for i in range(len(strs)):\n            body = "".join([s[st + len(strs[i]):], s[0:st]])\n            for p in strs[i], strs[i][::-1]:\n                for j in range(len(strs[i])):\n                    if p[j] >= result[0]:\n                        result = max(result, "".join([p[j:], body, p[:j]]))\n            st += len(strs[i])\n        return result\n\n'], 'label': ['n', 'n^2']}, [Path('/tests/scraping/leetcode/test_parse/mock_files/mock_files2/my-calendar-i.py'), Path('/tests/scraping/leetcode/test_parse/mock_files/mock_files1/complete-binary-tree-inserter.py')])


def test_parse_data(folder_path, expected_parsed_data) -> None:
    raw_data: MyDict = search_files(folder_path)

    got: tuple[dict[str, list[str]], list[Any]] = FileParser().parse_files(**raw_data)
    assert got == expected_parsed_data
