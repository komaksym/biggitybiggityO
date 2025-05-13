# Time:  O(m + n)

class Solution(object):
    def countNegatives(self, grid):
        result, c = 0, len(grid[0])-1
        for row in grid:
            while c >= 0 and row[c] < 0:
                c -= 1
            result += len(grid[0])-1-c
        return result
