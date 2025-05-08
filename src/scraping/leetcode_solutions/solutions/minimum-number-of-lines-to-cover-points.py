# Time:  O(n^2 + n*2^n) = O(n*2^n)

import collections


# math, hash table, bitmasks
class Solution(object):
    def minimumLines(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def gcd(a, b): 
            while b:
                a, b = b, a % b
            return a

        def popcount(x):
            result = 0
            while x:
                x &= (x-1)
                result += 1
            return result

        def ceil_divide(a, b):
            return (a+b-1)//b
        
        lookup = collections.defaultdict(set)               
        for i, (x1, y1) in enumerate(points):
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                a, b, c = (y2-y1), -(x2-x1), x1*(y2-y1)-y1*(x2-x1) 
                g = gcd(gcd(a, b), c)
                a, b, c = a//g, b//g, c//g
                lookup[(a, b, c)].add((x1, y1))
                lookup[(a, b, c)].add((x2, y2))
        lines = [l for l, p in lookup.items() if len(p) > 2] 
        assert(len(lines) <= (len(points))//2) 
        result = float("inf")
        for mask in range(1<<len(lines)):
            covered = set()
            bit, i = 1, 0
            while bit <= mask:
                if mask&bit:
                    covered.update(lookup[lines[i]])
                bit <<= 1                        
                i += 1
            result = min(result, popcount(mask) + ceil_divide(len(points)-len(covered), 2))
        return result
