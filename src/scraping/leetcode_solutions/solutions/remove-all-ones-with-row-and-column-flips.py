# Time:  O(m * n)

class Solution(object):
    def removeOnes(self, grid):
        
        return all(grid[i] == grid[0] or all(grid[i][j] != grid[0][j] for j in range(len(grid[0]))) for i in range(1, len(grid)))
