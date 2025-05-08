# Time:  O(nlogn)

import itertools


class Solution(object):
    def heightChecker(self, heights):
        
        return sum(i != j for i, j in zip(heights, sorted(heights)))
