# Time:  O(n)

import collections


# freq table
class Solution(object):
    def minimumOperationsToMakeKPeriodic(self, word, k):
        
        cnt = collections.Counter(word[i:i+k]for i in range(0, len(word), k))
        return len(word)//k-max(cnt.values())
