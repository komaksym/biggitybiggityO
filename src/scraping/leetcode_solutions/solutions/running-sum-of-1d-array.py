# Time:  O(n)

class Solution(object):
    def runningSum(self, nums):
        
        for i in range(len(nums)-1):
            nums[i+1] += nums[i]
        return nums
