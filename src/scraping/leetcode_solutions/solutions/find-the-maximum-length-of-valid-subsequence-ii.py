# Time:  O(n * k)

# dp
class Solution(object):
    def maximumLength(self, nums, k):
        result = 0
        for i in range(k):
            dp = [0]*k
            for x in nums:
                dp[x%k] = dp[(i-x)%k]+1
            result = max(result, max(dp))
        return result
