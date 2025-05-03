# Time:  O(n^2)
# Space: O(n^2)

import collections
import itertools


# hash table
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt1 = collections.Counter(tuple(row) for row in grid)
        cnt2 = collections.Counter(tuple(col) for col in zip(*grid))
        return sum(cnt1[k]*cnt2[k] for k in cnt1.keys() if k in cnt2)
