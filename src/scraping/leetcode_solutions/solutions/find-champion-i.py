# Time:  O(n^2)

# array
class Solution(object):
    def findChampion(self, grid):
        return next(u for u in range(len(grid)) if sum(grid[u]) == len(grid)-1)
