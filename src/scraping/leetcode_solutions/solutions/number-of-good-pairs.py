# Time:  O(n)

import collections


class Solution(object):
    def numIdenticalPairs(self, nums):
        
        return sum(c*(c-1)//2 for c in collections.Counter(nums).values())
