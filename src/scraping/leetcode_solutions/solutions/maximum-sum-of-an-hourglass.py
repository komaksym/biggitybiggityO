# Time:  O(m * n)

# brute force
class Solution(object):
    def maxSum(self, grid):
        def total(i, j):
            return (grid[i][j]+grid[i][j+1]+grid[i][j+2]+
                               grid[i+1][j+1]+
                    grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2])

        return max(total(i, j) for i in range(len(grid)-2) for j in range(len(grid[0])-2))
