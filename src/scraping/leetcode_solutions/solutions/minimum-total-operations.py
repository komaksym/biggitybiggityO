# Time:  O(n)

# array
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums[i] != nums[i+1] for i in range(len(nums)-1))
