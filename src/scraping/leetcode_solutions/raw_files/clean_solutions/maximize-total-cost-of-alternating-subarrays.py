# Time:  O(n)

# dp
class Solution(object):
    def maximumTotalCost(self, nums):
        dp = [nums[0], float("-inf")]
        for i in range(1, len(nums)):
            dp[:] = [max(dp)+nums[i], dp[0]-nums[i]]
        return max(dp)
