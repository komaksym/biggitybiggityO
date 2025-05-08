# Time:  O(n^2 * logn)

import fractions

class Solution(object):
    def simplifiedFractions(self, n):
        lookup = set()
        for b in range(1, n+1):
            for a in range(1, b):
                g = fractions.gcd(a, b)
                lookup.add((a//g, b//g))
        return ["{}/{}".format(*x) for x in lookup]
