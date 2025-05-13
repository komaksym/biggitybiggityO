# Time:  O(n)

class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [0] * 3
        for i in reversed(range(len(cost))):
            dp[i%3] = cost[i] + min(dp[(i+1)%3], dp[(i+2)%3])
        return min(dp[0], dp[1])

