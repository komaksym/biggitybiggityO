# Time:  O(m * n)
# Space: O(min(m, n))

# prefix sum
class Solution(object):
    def differenceOfDistinctValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        def update(i, j):
            lookup = set()
            for k in range(min(len(grid)-i, len(grid[0])-j)):
                result[i+k][j+k] = len(lookup)
                lookup.add(grid[i+k][j+k])
            lookup.clear()
            for k in reversed(range(min(len(grid)-i, len(grid[0])-j))):
                result[i+k][j+k] = abs(result[i+k][j+k]-len(lookup))
                lookup.add(grid[i+k][j+k])

        result = [[0]*len(grid[0]) for _ in range(len(grid))]
        for j in range(len(grid[0])):
            update(0, j)
        for i in range(1, len(grid)):
            update(i, 0)
        return result
