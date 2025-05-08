# Time:  O(n^2)

# dp
class Solution(object):
    def maximumJumps(self, nums, target):
        
        dp = [-1]*len(nums)
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if abs(nums[i]-nums[j]) <= target:
                    if dp[j] != -1:
                        dp[i] = max(dp[i], dp[j]+1)
        return dp[-1]
