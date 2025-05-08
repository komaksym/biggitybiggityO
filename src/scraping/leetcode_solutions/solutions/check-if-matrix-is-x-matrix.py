# Time:  O(n^2)

# array
class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        return all((i-j == 0 or i+j == len(grid)-1) == (grid[i][j] != 0) for i in range(len(grid)) for j in range(len(grid[0])))
