# Time:  O(n)

import collections


# freq table
class Solution(object):
    def maxFrequencyElements(self, nums):
        
        cnt = collections.Counter(nums)
        mx = max(cnt.values())
        return sum(v for v in cnt.values() if v == mx)
