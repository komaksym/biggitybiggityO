# Time:  O(n)

# array
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums, key=lambda x:(-abs(x), x))
