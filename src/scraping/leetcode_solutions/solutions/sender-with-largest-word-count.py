# Time:  O(n * l)

import collections
import itertools


# freq table
class Solution(object):
    def largestWordCount(self, messages, senders):
        
        cnt = collections.Counter()
        for m, s in zip(messages, senders):
            cnt[s] += m.count(' ')+1
        return max((k for k in cnt.keys()), key=lambda x: (cnt[x], x))
