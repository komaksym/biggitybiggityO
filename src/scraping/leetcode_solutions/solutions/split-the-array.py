# Time:  O(n)

import collections


# freq table
class Solution(object):
    def isPossibleToSplit(self, nums):
        return all(v <= 2 for v in collections.Counter(nums).values())
