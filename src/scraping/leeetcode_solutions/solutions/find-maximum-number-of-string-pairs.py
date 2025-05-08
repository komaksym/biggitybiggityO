# Time:  O(n)

import collections


# freq table
class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        
        result = 0
        cnt = collections.Counter()
        for w in words:
            result += cnt[w[::-1]]
            cnt[w] += 1
        return result
