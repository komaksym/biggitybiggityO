# Time:  O(n)

from operator import xor
from functools import reduce


class Solution(object):
    def xorGame(self, nums):
        return reduce(xor, nums) == 0 or \
            len(nums) % 2 == 0

