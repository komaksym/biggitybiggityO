# Time:  O(n)

# hash table
class Solution(object):
    def findFinalValue(self, nums, original):
        lookup = set(nums)
        while original in lookup:
            original *= 2
        return original
