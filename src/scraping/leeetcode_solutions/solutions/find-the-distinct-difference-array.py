# Time:  O(n)

# hash table, prefix sum
class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        lookup = set()
        for i in range(len(nums)):
            lookup.add(nums[i])
            result[i] = len(lookup)
        lookup.clear()
        for i in reversed(range(len(nums))):
            result[i] -= len(lookup)
            lookup.add(nums[i])
        return result
