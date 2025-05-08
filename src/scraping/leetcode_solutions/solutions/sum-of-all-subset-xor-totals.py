# Time:  O(n)
# Space: O(1)

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for x in nums:
            result |= x
        return result * 2**(len(nums)-1)
