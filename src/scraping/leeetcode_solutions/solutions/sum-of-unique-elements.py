# Time:  O(n)

import collections


class Solution(object):
    def sumOfUnique(self, nums):
        
        return sum(x for x, c in collections.Counter(nums).items() if c == 1)
