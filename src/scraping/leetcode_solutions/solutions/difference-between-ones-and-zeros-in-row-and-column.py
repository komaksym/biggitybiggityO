# Time:  O(m * n)

# array
class Solution(object):
    def onesMinusZeros(self, grid):
        rows = [sum(grid[i][j] for j in range(len(grid[0]))) for i in range(len(grid))]
        cols = [sum(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        return [[rows[i]+cols[j]-(len(grid)-rows[i])-(len(grid[0])-cols[j]) for j in range(len(grid[0]))] for i in range(len(grid))]
