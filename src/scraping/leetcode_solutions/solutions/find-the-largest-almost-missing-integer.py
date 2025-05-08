# Time:  O(n)

import collections


# freq table
class Solution(object):
    def largestInteger(self, nums, k):
        if k == len(nums):
            return max(nums)
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1
        if k == 1:
            return max(x for x, v in cnt.items() if v == 1) if any(v == 1 for v in cnt.values()) else -1
        result = -1
        if cnt[nums[0]] == 1:
            result = max(result, nums[0])
        if cnt[nums[-1]] == 1:
            result = max(result, nums[-1])
        return result
