# Time:  O(m * nlogn)

# sort
class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        for row in nums:
            row.sort()
        return sum(max(nums[r][c] for r in range(len(nums))) for c in range(len(nums[0])))
