# Time:  O(n)

# constructive algorithms
class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        return len(nums) <= 2 or any(nums[i]+nums[i+1] >= m for i in range(len(nums)-1))
