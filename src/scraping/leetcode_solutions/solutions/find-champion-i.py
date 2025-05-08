# Time:  O(n^2)

# array
class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return next(u for u in range(len(grid)) if sum(grid[u]) == len(grid)-1)
