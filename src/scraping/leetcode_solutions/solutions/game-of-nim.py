# Time:  O(n)

import operator
from functools import reduce


class Solution(object):
    def nimGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return reduce(operator.xor, piles, 0)
