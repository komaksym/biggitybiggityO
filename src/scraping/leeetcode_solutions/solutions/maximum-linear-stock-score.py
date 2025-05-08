# Time:  O(n)

import collections


# math, freq table
class Solution(object):
    def maxScore(self, prices):
        
        cnt = collections.Counter()
        for i, x in enumerate(prices):
            cnt[x-i] += x
        return max(cnt.values())
