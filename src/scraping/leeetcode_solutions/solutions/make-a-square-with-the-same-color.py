# Time:  O((n - w + 1)^2 * w^2)

import collections


# array
class Solution(object):
    def canMakeSquare(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        N, W = 3, 2
        return any(max(collections.Counter(grid[i+h][j+w] for h in range(W) for w in range(W)).values()) >= W**2-1
                   for i in range(N-W+1) for j in range(N-W+1))
