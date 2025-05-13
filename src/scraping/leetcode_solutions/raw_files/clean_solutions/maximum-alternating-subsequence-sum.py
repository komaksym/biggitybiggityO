# Time:  O(n)

class Solution(object):
    def maxAlternatingSum(self, nums):
        result = nums[0]
        for i in range(len(nums)-1):
            result += max(nums[i+1]-nums[i], 0)
        return result
