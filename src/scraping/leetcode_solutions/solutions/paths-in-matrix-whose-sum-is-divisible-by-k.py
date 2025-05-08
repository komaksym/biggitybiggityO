# Time:  O(m * n * k)
# Space: O(n * k)

# dp
class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[0 for _ in range(k)] for _ in range(len(grid[0]))]
        dp[0][0] = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[j] = [((dp[j-1][(l-grid[i][j])%k] if j-1 >= 0 else 0)+dp[j][(l-grid[i][j])%k])%MOD for l in range(k)]
        return dp[-1][0]
