# Time:  O(n * k)

import collections


# freq table
class Solution(object):
    def countPairs(self, coordinates, k):
        result = 0
        cnt = collections.Counter()
        for x, y in coordinates:
            for i in range(k+1):
                result += cnt.get((x^i, y^(k-i)), 0)
            cnt[(x, y)] += 1
        return result
