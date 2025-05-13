# Time:  O(n * l)

import collections


# hash table, freq table
class Solution(object):
    def findCommonResponse(self, responses):
        cnt = collections.defaultdict(int)
        for r in responses:
            for x in set(r):
                cnt[x] += 1
        return min((-c, x) for x, c in cnt.items())[1]
