# Time:  O(n)

# prefix sum, greedy
class Solution(object):
    def maximumOr(self, nums, k):
        
        right = [0]*(len(nums)+1)
        for i in reversed(range(len(nums))):
            right[i] = right[i+1]|nums[i]
        result = left = 0
        for i in range(len(nums)):
            result = max(result, left|(nums[i]<<k)|right[i+1])
            left |= nums[i]
        return result
