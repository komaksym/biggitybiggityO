# Time:  O(c), c = len(coordinates)

import collections


# freq table
class Solution(object):
    def countBlackBlocks(self, m, n, coordinates):
        
        L = 2

        cnt = collections.Counter()
        for x, y in coordinates:
            for nx in range(max(x-(L-1), 0), min(x+1, m-(L-1))):
                for ny in range(max(y-(L-1), 0), min(y+1, n-(L-1))):
                    cnt[nx, ny] += 1
        result = [0]*(L**2+1)
        for c in cnt.values():
            result[c] += 1
        result[0] = (m-(L-1))*(n-(L-1))-sum(result[i] for i in range(1, len(result)))
        return result
