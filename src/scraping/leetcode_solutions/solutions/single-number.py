# Time:  O(n)

import operator
from functools import reduce


class Solution(object):
    def singleNumber(self, A):
        return reduce(operator.xor, A)

