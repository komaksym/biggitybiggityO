# Time:  O(m * n)

import collections


class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        count = collections.Counter(tuple(x^row[0] for x in row)
                                          for row in matrix)
        return max(count.values())
