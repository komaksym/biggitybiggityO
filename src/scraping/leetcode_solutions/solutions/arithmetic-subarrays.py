# Time:  O(n * q)

import itertools


class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        
        def is_arith(n):
            mx, mn, lookup = max(n), min(n), set(n)
            if mx == mn:
                return True
            d, r = divmod(mx-mn, len(n)-1)
            if r:
                return False
            return all(i in lookup for i in range(mn, mx, d))
    
        result = []
        for left, right in zip(l, r):
            result.append(is_arith(nums[left:right+1]))
        return result
