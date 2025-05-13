# Time:  O(n^2)

class Solution(object):
    def probabilityOfHeads(self, prob, target):
        dp = [0.0]*(target+1)
        dp[0] = 1.0
        for p in prob:
            for i in reversed(range(target+1)):
                dp[i] = (dp[i-1] if i >= 1 else 0.0)*p + dp[i]*(1-p)
        return dp[target]
