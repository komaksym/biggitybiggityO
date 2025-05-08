# Time:  O(m * n)

# dp
class Solution(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        POS_INF = float("inf")
        NEG_INF = float("-inf")
        result = NEG_INF
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mn = POS_INF
                if i-1 >= 0:
                    mn = min(mn, grid[i-1][j])
                if j-1 >= 0:
                    mn = min(mn, grid[i][j-1])
                result = max(result, grid[i][j]-mn)
                grid[i][j] = min(grid[i][j], mn)
        return result
