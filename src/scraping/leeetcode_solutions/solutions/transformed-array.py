# Time:  O(n)

# array
class Solution(object):
    def constructTransformedArray(self, nums):
        
        return [nums[(i+nums[i])%len(nums)] for i in range(len(nums))]
