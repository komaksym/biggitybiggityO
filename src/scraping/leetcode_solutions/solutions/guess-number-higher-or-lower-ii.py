# Time:  O(n^3)
# Space: O(n^2)
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(n+1)]  # dp[i][j]: min pay in [i+1, j+1)
        for j in range(n+1):
            for i in reversed(range(j-1)):
                dp[i][j] = min((k+1) + max(dp[i][k], dp[k+1][j]) for k in range(i, j))
        return dp[0][n]


# Time:  O(n^3)
# Space: O(n^2)
class Solution2(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(n+1)]  # dp[i][j]: min pay in [i+1, j+1)
        for i in reversed(range(n)):
            for j in range(i+2, n+1):
                dp[i][j] = min((k+1) + max(dp[i][k], dp[k+1][j]) for k in range(i, j))
        return dp[0][n]
