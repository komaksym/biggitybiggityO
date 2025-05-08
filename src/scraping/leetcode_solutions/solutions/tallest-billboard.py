# Time:  O(n * 3^(n/2))

import collections


class Solution(object):
    def tallestBillboard(self, rods):
        
        def dp(A):
            lookup = collections.defaultdict(int)
            lookup[0] = 0
            for x in A:
                for d, y in list(lookup.items()):
                    lookup[d+x] = max(lookup[d+x], y)
                    lookup[abs(d-x)] = max(lookup[abs(d-x)], y + min(d, x))
            return lookup

        left, right = dp(rods[:len(rods)//2]), dp(rods[len(rods)//2:])
        return max(left[d]+right[d]+d for d in left if d in right)
