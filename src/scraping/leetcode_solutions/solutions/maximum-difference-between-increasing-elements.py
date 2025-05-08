# Time:  O(n)

class Solution(object):
    def maximumDifference(self, nums):
        result, prefix = 0, float("inf")
        for x in nums: 
            result = max(result, x-prefix)
            prefix = min(prefix, x)
        return result if result else -1
