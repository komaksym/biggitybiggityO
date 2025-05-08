# Time:  O(n)

# array
class Solution(object):
    def isArraySpecial(self, nums):
        
        return all(nums[i]&1 != nums[i+1]&1 for i in range(len(nums)-1))
