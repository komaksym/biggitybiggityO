# Time:  O(n)

import operator
from functools import reduce


class Solution(object):
    def nimGame(self, piles):
        
        return reduce(operator.xor, piles, 0)
