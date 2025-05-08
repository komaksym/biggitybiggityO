# Time:  O(n^2)

import itertools


# knapsack dp
class Solution(object):
    def paintWalls(self, cost, time):
        dp = [float("inf")]*(len(cost)+1)
        dp[0] = 0
        for c, t in zip(cost, time):
            for j in reversed(range(1, len(cost)+1)):
                dp[j] = min(dp[j], dp[max(j-(t+1), 0)]+c)
        return dp[-1]
