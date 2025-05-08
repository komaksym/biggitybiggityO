# Time:  O(n)

import itertools


class Solution(object):
    def gridGame(self, grid):
        result = float("inf")
        left, right = 0, sum(grid[0])
        for a, b in zip(grid[0], grid[1]):
            right -= a
            result = min(result, max(left, right))
            left += b
        return result
