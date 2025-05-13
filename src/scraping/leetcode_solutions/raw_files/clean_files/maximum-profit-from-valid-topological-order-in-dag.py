# Time:  O(n * 2^n)

# dp, bitmasks
class Solution(object):
    def maxProfit(self, n, edges, score):
        def popcount(x):
            return bin(x).count('1')

        adj = [0]*n
        for i, j in edges:
            adj[j] |= 1<<i
        dp = [-1]*(1<<n)
        dp[0] = 0 
        for mask in range(1<<n):
            if dp[mask] == -1:
                continue
            l = popcount(mask)+1
            for i in range(n):
                if mask&(1<<i):
                    continue
                if (mask & adj[i]) == adj[i]: 
                    dp[mask|(1<<i)] = max(dp[mask|(1<<i)], dp[mask]+l*score[i])
        return dp[-1]
