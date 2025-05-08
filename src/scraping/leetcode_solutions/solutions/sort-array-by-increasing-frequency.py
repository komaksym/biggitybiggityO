# Time:  O(nlogn)

import collections


class Solution(object):
    def frequencySort(self, nums):
        count = collections.Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))
