# Time:  O(n)

# dp
class Solution(object):
    def maxScore(self, a, b):
        dp = [float("-inf")]*(len(a)+1)
        dp[0] = 0
        for x in b:
            for i in reversed(range(1, len(dp))):
                dp[i] = max(dp[i], dp[i-1]+x*a[i-1])
        return dp[-1]
