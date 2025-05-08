# Time:  O(n + m), m is the max number of nums

import collections


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = collections.Counter(nums)
        for i in range(max(nums)+1):
            count[i] += count[i-1]
        return [count[i-1] for i in nums]


# Time:  O(nlogn)
import bisect


class Solution2(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        return [bisect.bisect_left(sorted_nums, i) for i in nums]
