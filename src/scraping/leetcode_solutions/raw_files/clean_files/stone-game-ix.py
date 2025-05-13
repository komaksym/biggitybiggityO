# Time:  O(n)

import collections


class Solution(object):
    def stoneGameIX(self, stones):
        count = collections.Counter(x%3 for x in stones)
        if count[0]%2 == 0:
            return count[1] and count[2]
        return abs(count[1]-count[2]) >= 3  
