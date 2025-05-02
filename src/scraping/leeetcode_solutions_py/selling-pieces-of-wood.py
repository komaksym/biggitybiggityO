# Time:  O(m * n * (m + n))
# Space: O(m * n)

# dp
class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """
        dp = [[0]*(n+1) for i in range(m+1)]
        for h, w, p in prices:
            dp[h][w] = p
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(1, i//2+1):
                    dp[i][j] = max(dp[i][j], dp[k][j]+dp[i-k][j])
                for k in range(1, j//2+1):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[i][j-k])
        return dp[m][n]
