# Time:  O(n * a * c), n = len(price), a = maxAmount, c = maxCoupons

import itertools


# dp
class Solution(object):
    def maxTastiness(self, price, tastiness, maxAmount, maxCoupons):
        
        dp = [[0]*(maxCoupons+1) for _ in range(maxAmount+1)]
        for p, t in zip(price, tastiness):
            for i in reversed(range(p//2, maxAmount+1)):
                for j in reversed(range(maxCoupons+1)):
                    if i-p >= 0:
                        dp[i][j] = max(dp[i][j], t+dp[i-p][j])
                    if j-1 >= 0:
                        dp[i][j] = max(dp[i][j], t+dp[i-p//2][j-1])
        return dp[maxAmount][maxCoupons]
