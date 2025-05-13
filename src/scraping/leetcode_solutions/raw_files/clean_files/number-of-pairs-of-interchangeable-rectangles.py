# Time:  O(n)

import collections
import fractions


class Solution(object):
    def interchangeableRectangles(self, rectangles):
        count = collections.defaultdict(int)
        for w, h in rectangles:
            g = fractions.gcd(w, h) 
            count[(w//g, h//g)] += 1
        return sum(c*(c-1)//2 for c in count.values())
