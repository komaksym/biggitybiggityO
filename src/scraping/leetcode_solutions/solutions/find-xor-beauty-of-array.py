# Time:  O(n)

import operator
from functools import reduce


# bit manipulation, math
class Solution(object):
    def xorBeauty(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)
