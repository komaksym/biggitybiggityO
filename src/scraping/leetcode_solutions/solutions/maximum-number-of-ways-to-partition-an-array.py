# Time:  O(n)

import collections


class Solution(object):
    def waysToPartition(self, nums, k):
        total = sum(nums)
        right = collections.Counter()
        prefix = 0
        for i in range(len(nums)-1):
            prefix += nums[i]
            right[prefix-(total-prefix)] += 1
        result = right[0]
        left = collections.Counter()
        prefix = 0
        for x in nums:
            result = max(result, left[k-x]+right[-(k-x)])
            prefix += x
            left[prefix-(total-prefix)] += 1
            right[prefix-(total-prefix)] -= 1
        return result
