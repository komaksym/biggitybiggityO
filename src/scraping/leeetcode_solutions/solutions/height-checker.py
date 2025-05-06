# Time:  O(nlogn)

import itertools


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(i != j for i, j in zip(heights, sorted(heights)))
