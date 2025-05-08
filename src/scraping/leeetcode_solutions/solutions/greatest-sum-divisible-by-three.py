# Time:  O(n)

class Solution(object):
    def maxSumDivThree(self, nums):
        
        dp = [0, 0, 0]
        for num in nums:
            for i in [num+x for x in dp]:
                dp[i%3] = max(dp[i%3], i)
        return dp[0]
