from functools import reduce
# Time:  O(m * 2^n)

# bitmasks, constructive algorithms, greedy
class Solution(object):
    def goodSubsetofBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        lookup = {}
        for i in range(len(grid)):
            mask = reduce(lambda mask, j: mask|(grid[i][j]<<j), range(len(grid[0])), 0)
            if not mask:
                return [i]
            for mask2, j in lookup.items():
                if mask2&mask == 0:
                    return [j, i]
            lookup[mask] = i
        return []
