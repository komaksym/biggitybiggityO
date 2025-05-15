import pytest
from ...src.clean import search_files, clean_files
from pathlib import PosixPath
import re


@pytest.fixture
def folder_path():
    return "leetcode_solutions/tests/test_clean/mock_files/"


@pytest.fixture
def expected_raw_data():
    return {
        "file_paths": [
            PosixPath(
                "leetcode_solutions/tests/test_clean/mock_files/mock_subfolder2/random-pick-index.py"
            ),
            PosixPath(
                "leetcode_solutions/tests/test_clean/mock_files/mock_subfolder2/empty_file.py"
            ),
            PosixPath(
                "leetcode_solutions/tests/test_clean/mock_files/mock_subfolder1/bitwise-and-of-numbers-range.py"
            ),
            PosixPath(
                "leetcode_solutions/tests/test_clean/mock_files/mock_subfolder1/closest-dessert-cost.py"
            ),
        ],
        "files": [
            "# Time:  ctor: O(n)\n#        pick: O(1)\n\nfrom random import randint\nimport collections\n\n\nclass Solution(object):\n\n    def __init__(self, nums):\n        self.__lookup = collections.defaultdict(list)\n        for i, x in enumerate(nums):\n            self.__lookup[x].append(i)\n\n    def pick(self, target):\n        return self.__lookup[target][randint(0, len(self.__lookup[target])-1)]\n\n\n# Time:  ctor: O(1)\n#        pick: O(n)\nfrom random import randint\n\n\nclass Solution_TLE(object):\n\n    def __init__(self, nums):\n        self.__nums = nums\n\n    def pick(self, target):\n        reservoir = -1\n        n = 0\n        for i in range(len(self.__nums)):\n            if self.__nums[i] != target:\n                continue\n            reservoir = i if randint(1, n+1) == 1 else reservoir\n            n += 1\n        return reservoir\n\n\n\n",
            "",
            "# Time:  O(1)\n\nclass Solution(object):\n    def rangeBitwiseAnd(self, m, n):\n        while m < n:\n            n &= n - 1\n        return n\n\n\nclass Solution2(object):\n    def rangeBitwiseAnd(self, m, n):\n        i, diff = 0, n-m\n        while diff:\n            diff >>= 1\n            i += 1\n        return n & m >> i << i\n\n",
            'class Solution(object):\n    def closestCost(self, baseCosts, toppingCosts, target):\n        max_count = 2\n        max_base, max_topping = max(baseCosts), max(toppingCosts)\n        dp = [False]*(max(max_base, target+max_topping//2)+1)\n        for b in baseCosts:\n            dp[b] = True\n        for t in toppingCosts:\n            for _ in range(max_count):\n                for i in reversed(range(len(dp)-t)):\n                    if dp[i]:\n                        dp[i+t] = True\n        result = float("inf")\n        for i in range(1, len(dp)):\n            if not dp[i]:\n                continue\n            if abs(i-target) < abs(result-target):\n                result = i\n            if i >= target:\n                break\n        return result\n    \n    \nclass Solution2(object):\n    def closestCost(self, baseCosts, toppingCosts, target):\n        max_count = 2\n        def backtracking(toppingCosts, i, cost, target, lookup, result):\n            if (i, cost) in lookup:\n                return\n            lookup.add((i, cost))\n            if cost >= target or i == len(toppingCosts):\n                if (abs(cost-target), cost) < (abs(result[0]-target), result[0]):\n                    result[0] = cost\n                return\n            for j in range(max_count+1):\n                backtracking(toppingCosts, i+1, cost+j*toppingCosts[i], target, lookup, result)\n\n        result = [float("inf")]\n        lookup = set()\n        for b in baseCosts:\n            backtracking(toppingCosts, 0, b, target, lookup, result)\n        return result[0]\n\n\n# Time:  O(3^m*log(3^m)) + O(n*log(3^m)) = O(m*(3^m + n))\nimport bisect\n\n\nclass Solution3(object):\n    def closestCost(self, baseCosts, toppingCosts, target):\n        max_count = 2\n        combs = set([0])\n        for t in toppingCosts:\n            combs = set([c+i*t for c in combs for i in range(max_count+1)])\n        result, combs = float("inf"), sorted(combs)\n        for b in baseCosts:\n            idx = bisect.bisect_left(combs, target-b)\n            if idx < len(combs):\n                result = min(result, b+combs[idx], key=lambda x: (abs(x-target), x))\n            if idx > 0:\n                result = min(result, b+combs[idx-1], key=lambda x: (abs(x-target), x))        \n        return result\n\n\n# Time:  O(n * 3^m)\nclass Solution4(object):\n    def closestCost(self, baseCosts, toppingCosts, target):\n        max_count = 2\n        combs = set([0])\n        for t in toppingCosts:\n            combs = set([c+i*t for c in combs for i in range(max_count+1)])\n        result = float("inf")\n        for b in baseCosts:\n            for c in combs:\n                result = min(result, b+c, key=lambda x: (abs(x-target), x))      \n        return result\n',
        ],
    }


def test_search_files(folder_path, expected_raw_data):
    got = search_files(folder_path)

    assert got == expected_raw_data


@pytest.fixture
def filter_pattern():
    return re.compile(
        r"(#.*?$)|(\"{3}.*?\"{3})|('{3}.*?'{3})",
        flags=re.DOTALL | re.IGNORECASE | re.MULTILINE,
    )


@pytest.fixture
def expected_parsed_data():
    return {
        "code": [
            "class Solution(object):\n\n    def __init__(self, nums):\n        self.__lookup = collections.defaultdict(list)\n        for i, x in enumerate(nums):\n            self.__lookup[x].append(i)\n\n    def pick(self, target):\n        return self.__lookup[target][randint(0, len(self.__lookup[target])-1)]\n\n",
            "class Solution_TLE(object):\n\n    def __init__(self, nums):\n        self.__nums = nums\n\n    def pick(self, target):\n        reservoir = -1\n        n = 0\n        for i in range(len(self.__nums)):\n            if self.__nums[i] != target:\n                continue\n            reservoir = i if randint(1, n+1) == 1 else reservoir\n            n += 1\n        return reservoir\n\n\n",
            "class Solution(object):\n    def rangeBitwiseAnd(self, m, n):\n        while m < n:\n            n &= n - 1\n        return n\n\n",
            "class Solution2(object):\n    def rangeBitwiseAnd(self, m, n):\n        i, diff = 0, n-m\n        while diff:\n            diff >>= 1\n            i += 1\n        return n & m >> i << i\n",
            'class Solution(object):\n    def closestCost(self, baseCosts, toppingCosts, target):\n        max_count = 2\n        max_base, max_topping = max(baseCosts), max(toppingCosts)\n        dp = [False]*(max(max_base, target+max_topping//2)+1)\n        for b in baseCosts:\n            dp[b] = True\n        for t in toppingCosts:\n            for _ in range(max_count):\n                for i in reversed(range(len(dp)-t)):\n                    if dp[i]:\n                        dp[i+t] = True\n        result = float("inf")\n        for i in range(1, len(dp)):\n            if not dp[i]:\n                continue\n            if abs(i-target) < abs(result-target):\n                result = i\n            if i >= target:\n                break\n        return result\n    \n    ',
            'class Solution2(object):\n    def closestCost(self, baseCosts, toppingCosts, target):\n        max_count = 2\n        def backtracking(toppingCosts, i, cost, target, lookup, result):\n            if (i, cost) in lookup:\n                return\n            lookup.add((i, cost))\n            if cost >= target or i == len(toppingCosts):\n                if (abs(cost-target), cost) < (abs(result[0]-target), result[0]):\n                    result[0] = cost\n                return\n            for j in range(max_count+1):\n                backtracking(toppingCosts, i+1, cost+j*toppingCosts[i], target, lookup, result)\n\n        result = [float("inf")]\n        lookup = set()\n        for b in baseCosts:\n            backtracking(toppingCosts, 0, b, target, lookup, result)\n        return result[0]\n\n',
            'class Solution3(object):\n    def closestCost(self, baseCosts, toppingCosts, target):\n        max_count = 2\n        combs = set([0])\n        for t in toppingCosts:\n            combs = set([c+i*t for c in combs for i in range(max_count+1)])\n        result, combs = float("inf"), sorted(combs)\n        for b in baseCosts:\n            idx = bisect.bisect_left(combs, target-b)\n            if idx < len(combs):\n                result = min(result, b+combs[idx], key=lambda x: (abs(x-target), x))\n            if idx > 0:\n                result = min(result, b+combs[idx-1], key=lambda x: (abs(x-target), x))        \n        return result\n\n',
            'class Solution4(object):\n    def closestCost(self, baseCosts, toppingCosts, target):\n        max_count = 2\n        combs = set([0])\n        for t in toppingCosts:\n            combs = set([c+i*t for c in combs for i in range(max_count+1)])\n        result = float("inf")\n        for b in baseCosts:\n            for c in combs:\n                result = min(result, b+c, key=lambda x: (abs(x-target), x))      \n        return result',
        ],
        "label": [
            "# Time:  ctor: O(n)\n#        pick: O(1)",
            "# Time:  ctor: O(1)\n#        pick: O(n)",
            "# Time:  O(1)",
            "# Time:  O(1)",
            "",
            "",
            "# Time:  O(3^m*log(3^m)) + O(n*log(3^m)) = O(m*(3^m + n))",
            "# Time:  O(n * 3^m)",
        ],
    }


@pytest.fixture
def expected_corrupted_data():
    return []


def test_clean_files(
    expected_raw_data, expected_parsed_data, expected_corrupted_data, filter_pattern
):
    files, file_paths = expected_raw_data["files"], expected_raw_data["file_paths"]
    parsed_data, corrupted_data = clean_files(files, file_paths, filter_pattern)

    assert (parsed_data == expected_parsed_data) and (
        corrupted_data == expected_corrupted_data
    )