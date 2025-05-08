# Time:  O(n)

# prefix sum, greedy
class Solution(object):
    def maxScore(self, nums):
        
        result = mx = 0
        for i in reversed(range(1, len(nums))):
            mx = max(mx, nums[i])
            result += mx
        return result


# Time:  O(n^2)
# dp
class Solution2(object):
    def maxScore(self, nums):
        
        dp = [0]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                dp[i] = max(dp[i], dp[j]+(i-j)*nums[i])
        return dp[-1]
