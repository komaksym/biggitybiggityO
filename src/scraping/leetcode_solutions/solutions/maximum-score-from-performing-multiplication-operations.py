# Time:  O(m^2)

class Solution(object):
    def maximumScore(self, nums, multipliers):
        dp = [0]*(len(multipliers)+1)
        for l, m in enumerate(reversed(multipliers), start=len(nums)-len(multipliers)):
            dp = [max(m*nums[i]+dp[i+1], m*nums[i+l]+dp[i]) for i in range(len(dp)-1)]
        return dp[0]
