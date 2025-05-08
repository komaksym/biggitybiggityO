# Time:  O(nlogn)

# knapsack dp
class Solution(object):
    def numberOfWays(self, n, x):
        
        MOD = 10**9+7

        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            i_pow_x = i**x
            if i_pow_x > n:
                break
            for j in reversed(range(i_pow_x, n+1)):
                dp[j] = (dp[j]+dp[j-i_pow_x])%MOD
        return dp[-1]
