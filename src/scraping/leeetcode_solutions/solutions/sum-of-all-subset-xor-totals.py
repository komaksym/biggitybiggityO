# Time:  O(n)

class Solution(object):
    def subsetXORSum(self, nums):
        
       
       
       
       
        result = 0
        for x in nums:
            result |= x
        return result * 2**(len(nums)-1)
