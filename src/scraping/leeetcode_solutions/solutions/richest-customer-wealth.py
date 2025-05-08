# Time:  O(m * n)

import itertools


class Solution(object):
    def maximumWealth(self, accounts):
        
        return max(map(sum, accounts))
