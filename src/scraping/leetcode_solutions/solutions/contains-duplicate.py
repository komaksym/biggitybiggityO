# Time:  O(n)
# Space: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))

