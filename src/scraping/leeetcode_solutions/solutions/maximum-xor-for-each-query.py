# Time:  O(n)

class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        
        result = [0]*len(nums)
        mask = 2**maximumBit-1
        for i in range(len(nums)):
            mask ^= nums[i]
            result[-1-i] = mask
        return result
