# Time:  O(n)

# math
class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        mx = max(nums)
        return sum(mn < x < mx for x in nums)
