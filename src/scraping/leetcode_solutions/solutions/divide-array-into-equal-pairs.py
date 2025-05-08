# Time:  O(n)

import collections


# freq table
class Solution(object):
    def divideArray(self, nums):
        return all(cnt%2 == 0 for cnt in collections.Counter(nums).values())
