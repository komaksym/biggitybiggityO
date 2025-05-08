# Time:  O(n)

import itertools


# dp
class Solution(object):
    def minimumCosts(self, regular, express, expressCost):
        """
        :type regular: List[int]
        :type express: List[int]
        :type expressCost: int
        :rtype: List[int]
        """
        result = []
        dp = [0, expressCost] 
        for r, e in zip(regular, express):
            dp = [min(dp[0]+r, dp[1]+e), min(dp[0]+(r+expressCost), dp[1]+e)]
            result.append(min(dp[0], dp[1]))
        return result
