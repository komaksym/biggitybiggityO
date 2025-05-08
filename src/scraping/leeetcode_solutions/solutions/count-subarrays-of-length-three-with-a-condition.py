# Time:  O(n)

# array
class Solution(object):
    def countSubarrays(self, nums):
        
        return sum((nums[i-1]+nums[i+1])*2 == nums[i] for i in range(1, len(nums)-1))
