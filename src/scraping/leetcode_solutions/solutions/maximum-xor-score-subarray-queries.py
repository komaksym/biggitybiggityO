# Time:  O(n^2 + q)

# dp
class Solution(object):
    def maximumSubarrayXor(self, nums, queries):
        dp = [[nums[i] if j == 0 else 0 for j in range(len(nums)-i)] for i in range(len(nums))]
        for i in reversed(range(len(nums))):
            for l in range(1, len(nums)-i):
                dp[i][l] = dp[i][l-1]^dp[i+1][l-1]
        for i in reversed(range(len(nums))):
            for l in range(1, len(nums)-i):
                dp[i][l] = max(dp[i][l], dp[i][l-1], dp[i+1][l-1])
        return [dp[i][j-i] for i, j in queries]


# Time:  O(n^2 + q)
# dp
class Solution2(object):
    def maximumSubarrayXor(self, nums, queries):
        dp = [[nums[i] if i == j else 0 for j in range(len(nums))] for i in range(len(nums))]
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                dp[i][j] = dp[i][j-1]^dp[i+1][j]
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i+1][j])
        return [dp[i][j] for i, j in queries]
