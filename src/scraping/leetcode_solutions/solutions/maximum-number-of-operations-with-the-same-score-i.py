# Time:  O(n)

# array
class Solution(object):
    def maxOperations(self, nums):
        
        result = 1
        target = nums[0]+nums[1]
        for i in range(2, len(nums)-1, 2):
            if nums[i]+nums[i+1] != target:
                break
            result += 1
        return result
