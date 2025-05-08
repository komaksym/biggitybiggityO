# Time:  O(n)

import collections


class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        
        k = 3
        cnt1, cnt2 = collections.Counter(word1), collections.Counter(word2)
        return all(abs(cnt1[c]-cnt2[c]) <= k for c in set(list(cnt1.keys())+list(cnt2.keys())))

