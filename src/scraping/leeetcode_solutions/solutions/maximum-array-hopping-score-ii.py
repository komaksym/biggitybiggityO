# Time:  O(n)

# prefix sum, greedy
class Solution(object):
    def maxScore(self, nums):
        
        result = mx = 0
        for i in reversed(range(1, len(nums))):
            mx = max(mx, nums[i])
            result += mx
        return result
