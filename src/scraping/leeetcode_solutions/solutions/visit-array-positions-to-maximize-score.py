# Time:  O(n)

# dp
class Solution(object):
    def maxScore(self, nums, x):
        
        dp = [float("-inf")]*2
        dp[nums[0]%2] = nums[0]
        for i in range(1, len(nums)):
            dp[nums[i]%2] = max(dp[nums[i]%2], dp[(nums[i]+1)%2]-x)+nums[i]
        return max(dp)
