# Time:  O(n)
# Space: O(n)

import collections


# freq table
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        mx = max(cnt.values())
        return sum(v for v in cnt.values() if v == mx)
