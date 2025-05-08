# Time:  O(k * n) = O(n)

# dp
class Solution(object):
    def minimumOperations(self, nums):
        
        k = 3

        dp = [0]*k
        for x in nums:
            dp[x-1] += 1
            for i in range(x, len(dp)):
                dp[i] = max(dp[i], dp[i-1])
        return len(nums)-dp[-1]
