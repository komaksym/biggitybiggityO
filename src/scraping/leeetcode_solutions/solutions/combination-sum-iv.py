# Time:  O(nlon + n * t), t is the value of target.

class Solution(object):
    def combinationSum4(self, nums, target):
        
        dp = [0] * (target+1)
        dp[0] = 1
        nums.sort()

        for i in range(1, target+1):
            for j in range(len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]
                else:
                    break

        return dp[target]

