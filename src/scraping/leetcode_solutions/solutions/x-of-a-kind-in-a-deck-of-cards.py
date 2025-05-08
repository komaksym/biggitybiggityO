# Time:  O(n * (logn)^2)
# Space: O(n)

import collections
from functools import reduce


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b): 
            while b:
                a, b = b, a % b
            return a

        vals = list(collections.Counter(deck).values())
        return reduce(gcd, vals) >= 2

