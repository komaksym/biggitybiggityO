# Time:  O(n)

class Solution(object):
    def canDivideIntoSubsequences(self, nums, K):
        curr, max_count = 1, 1
        for i in range(1, len(nums)):
            curr = 1 if nums[i-1] < nums[i] else curr+1
            max_count = max(max_count, curr)
        return K*max_count <= len(nums)
