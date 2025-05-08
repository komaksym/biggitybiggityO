# Time:  O(n)

import operator
from functools import reduce


class Solution(object):
    def getXORSum(self, arr1, arr2):
        
        return reduce(operator.xor, arr1) & reduce(operator.xor, arr2)
