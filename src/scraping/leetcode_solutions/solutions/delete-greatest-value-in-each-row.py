# Time:  O(m * nlogn)

# array
class Solution(object):
    def deleteGreatestValue(self, grid):
        
        for row in grid:
            row.sort()
        return sum(max(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0])))
