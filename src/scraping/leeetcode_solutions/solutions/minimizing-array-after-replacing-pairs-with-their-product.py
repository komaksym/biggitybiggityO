# Time:  O(n)

# greedy
class Solution(object):
    def minArrayLength(self, nums, k):
        
        if 0 in nums:
            return 1
        result = len(nums)
        curr = nums[0]
        for i in range(1, len(nums)):
            if curr*nums[i] > k:
                curr = nums[i]
            else:
                curr *= nums[i]
                result -= 1
        return result
 
