# Time:  O(n)

class Solution(object):
    def maxAscendingSum(self, nums):
        result = curr = 0
        for i in range(len(nums)): 
            if not (i and nums[i-1] < nums[i]):
                curr = 0
            curr += nums[i]
            result = max(result, curr)
        return result
