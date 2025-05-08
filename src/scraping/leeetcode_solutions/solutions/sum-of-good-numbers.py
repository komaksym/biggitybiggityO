# Time:  O(n)

# array
class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        
        return sum(nums[i] for i in range(len(nums)) if (i-k < 0 or nums[i-k] < nums[i]) and (i+k >= len(nums) or nums[i+k] < nums[i]))
