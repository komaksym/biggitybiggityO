# Time:  O(n)

class Solution(object):
    def maxSubArray(self, nums):
        
        result, curr = float("-inf"), float("-inf")
        for x in nums:
            curr = max(curr+x, x)
            result = max(result, curr)
        return result
