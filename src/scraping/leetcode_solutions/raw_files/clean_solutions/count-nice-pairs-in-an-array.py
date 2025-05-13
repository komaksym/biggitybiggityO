# Time:  O(nlogm), m is max of nums

import collections


class Solution(object):
    def countNicePairs(self, nums):
        MOD = 10**9 + 7

        def rev(x):
            result = 0
            while x:
                x, r = divmod(x, 10)
                result = result*10+r
            return result
        
        result = 0
        lookup = collections.defaultdict(int)
        for num in nums:
            result = (result + lookup[num-rev(num)])%MOD
            lookup[num-rev(num)] += 1
        return result
