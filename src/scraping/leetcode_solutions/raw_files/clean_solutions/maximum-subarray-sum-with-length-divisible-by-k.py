# Time:  O(n)

# prefix sum, dp
class Solution(object):
    def maxSubarraySum(self, nums, k):
        dp = [float("inf")]*k
        dp[-1] = 0
        curr = 0
        result = float("-inf")
        for i, x in enumerate(nums):
            curr += x
            result = max(result, curr-dp[i%k])
            dp[i%k] = min(dp[i%k], curr)
        return result
