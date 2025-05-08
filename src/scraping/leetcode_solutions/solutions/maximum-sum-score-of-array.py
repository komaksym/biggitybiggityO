# Time:  O(n)

# prefix sum, math
class Solution(object):
    def maximumSumScore(self, nums):
        prefix = suffix = 0
        result = float("-inf")
        right = len(nums)-1
        for left in range(len(nums)):
            prefix += nums[left]
            suffix += nums[right]
            right -= 1
            result = max(result, prefix, suffix)
        return result

# prefix sum
class Solution2(object):
    def maximumSumScore(self, nums):
        total = sum(nums)
        prefix = 0
        result = float("-inf")
        for x in nums:
            prefix += x
            result = max(result, prefix, total-prefix+x)
        return result
