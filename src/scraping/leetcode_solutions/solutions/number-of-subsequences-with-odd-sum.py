# Time:  O(n)

# combinatorics, fast exponentiation
class Solution(object):
    def subsequenceCount(self, nums):
        MOD = 10**9+7
        return pow(2, len(nums)-1, MOD) if any(x%2 for x in nums) else 0


# Time:  O(n)
# dp
class Solution2(object):
    def subsequenceCount(self, nums):
        MOD = 10**9+7
        dp = [0]*2
        for x in nums:
            dp = [(dp[i]+dp[i^(x%2)]+int(x%2 == i))%MOD for i in range(2)]
        return dp[1]
