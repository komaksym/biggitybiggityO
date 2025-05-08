# Time:  O(m * n^2)

# dp
class Solution(object):
    def minPathCost(self, grid, moveCost):
        
        dp = [[0]*len(grid[0]) for _ in range(2)]
        dp[0] = [grid[0][j] for j in range(len(grid[0]))]
        for i in range(len(grid)-1):
            for j in range(len(grid[0])):
                dp[(i+1)%2][j] = min(dp[i%2][k]+moveCost[x][j] for k, x in enumerate(grid[i]))+grid[i+1][j]
        return min(dp[(len(grid)-1)%2])
