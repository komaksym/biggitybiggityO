# Time:  O(nlogn)

import itertools


# greedy, sort
class Solution(object):
    def minCost(self, arr, brr, k):
        """
        :type arr: List[int]
        :type brr: List[int]
        :type k: int
        :rtype: int
        """
        def cost():
            return sum(abs(x-y) for x, y in zip(arr, brr))

        result = cost()
        arr.sort()
        brr.sort()
        result = min(result, k+cost())
        return result
