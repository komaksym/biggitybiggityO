# Time:  O(logn)

import bisect


# binary search
class Solution(object):
    def maximumCount(self, nums):
        return max(bisect.bisect_left(nums, 0)-0, len(nums)-bisect.bisect_left(nums, 1))
