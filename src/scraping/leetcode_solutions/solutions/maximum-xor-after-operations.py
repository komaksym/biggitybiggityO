from functools import reduce
# Time:  O(n)

# bit manipulation
class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x|y, nums)
