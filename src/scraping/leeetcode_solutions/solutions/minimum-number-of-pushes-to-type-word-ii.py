# Time:  O(n)

import collections


# freq table, greedy
class Solution(object):
    def minimumPushes(self, word):
        
        return sum(x*(i//(9-2+1)+1) for i, x in enumerate(sorted(iter(collections.Counter(word).values()), reverse=True)))
