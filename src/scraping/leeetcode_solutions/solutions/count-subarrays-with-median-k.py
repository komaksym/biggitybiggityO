# Time:  O(n)

import collections


# freq table, prefix sum
class Solution(object):
    def countSubarrays(self, nums, k):
        
        idx = nums.index(k)
        lookup = collections.Counter()
        curr = 0
        for i in reversed(range(idx+1)):
            curr += 0 if nums[i] == k else -1 if nums[i] < k else +1
            lookup[curr] += 1
        result = curr = 0
        for i in range(idx, len(nums)):
            curr += 0 if nums[i] == k else -1 if nums[i] < k else +1
            result += lookup[-curr]+lookup[-(curr-1)]
        return result
