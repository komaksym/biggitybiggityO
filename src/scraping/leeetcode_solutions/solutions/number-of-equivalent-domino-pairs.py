# Time:  O(n)

import collections


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        
        counter = collections.Counter((min(x), max(x)) for x in dominoes)
        return sum(v*(v-1)//2 for v in counter.values())
