# Time:  O(n)

import collections


# freq table, constructive algorithms
class Solution(object):
    def minLengthAfterRemovals(self, nums):
        
        mx = max(collections.Counter(nums).values())
        return mx-(len(nums)-mx) if mx > (len(nums)-mx) else len(nums)%2
