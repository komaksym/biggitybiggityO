# Time:  O(n)

class Solution(object):
    def canBeIncreasing(self, nums):
        
        deleted = False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                continue
            if deleted:
                return False
            deleted = True
            if i >= 2 and nums[i-2] > nums[i]: 
                nums[i] = nums[i-1]
        return True
