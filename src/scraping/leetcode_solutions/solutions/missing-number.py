# Time:  O(n)

import operator
from functools import reduce


class Solution(object):
    def missingNumber(self, nums):
        return reduce(operator.xor, nums,
                      reduce(operator.xor, range(len(nums) + 1)))


class Solution2(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)

