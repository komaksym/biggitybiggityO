# Time:  O(n * k)

# dp, combinatorics
class Solution(object):
    def sumOfPower(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1
        for x in nums:
            for i in reversed(range(k+1)):
                dp[i] = (dp[i]+(dp[i]+(dp[i-x] if i-x >= 0 else 0)))%MOD
        return dp[k]
