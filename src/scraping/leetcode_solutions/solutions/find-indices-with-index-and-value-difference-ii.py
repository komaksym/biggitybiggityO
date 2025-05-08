# Time:  O(n)
# Space: O(1)

# prefix sum
class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        mx_i = mn_i = 0
        for i in range(len(nums)-indexDifference):
            if nums[i] > nums[mx_i]:
                mx_i = i
            elif nums[i] < nums[mn_i]:
                mn_i = i
            if nums[mx_i]-nums[i+indexDifference] >= valueDifference:
                return [mx_i, i+indexDifference]
            if nums[i+indexDifference]-nums[mn_i] >= valueDifference:
                return [mn_i, i+indexDifference]
        return [-1]*2
