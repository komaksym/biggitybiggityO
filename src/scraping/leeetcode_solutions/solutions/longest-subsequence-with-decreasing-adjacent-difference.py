# Time:  O(r^2 + n * r), r = max(nums)
# Space: O(r^2)

# dp
class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 2
        mx = max(nums)
        dp = [[0]*mx for _ in range(mx)]
        for x in nums:
            x -= 1
            for nx in range(len(dp[x])):
                d = abs(nx-x)
                dp[x][d] = max(dp[x][d], dp[nx][d]+1)
            for d in reversed(range(len(dp[x])-1)):
                dp[x][d] = max(dp[x][d], dp[x][d+1])
            result = max(result, dp[x][0])
        return result


# Time:  O(r^2 + n * r), r = max(nums)
# Space: O(r^2)
# dp
class Solution2(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 2
        mx = max(nums)
        dp = [[0]*mx for _ in range(mx)]
        for x in reversed(nums):
            x -= 1
            for nx in range(len(dp[x])):
                d = abs(nx-x)
                dp[x][d] = max(dp[x][d], dp[nx][d]+1)
            for d in range(1, len(dp[x])):
                dp[x][d] = max(dp[x][d], dp[x][d-1])
            result = max(result, dp[x][-1])
        return result
