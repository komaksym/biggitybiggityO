# Time:  O(n)

class Solution(object):
    def getMinDistance(self, nums, target, start):
        
        for i in range(len(nums)):
            if (start-i >= 0 and nums[start-i] == target) or \
               (start+i < len(nums) and nums[start+i] == target):
                break
        return i
