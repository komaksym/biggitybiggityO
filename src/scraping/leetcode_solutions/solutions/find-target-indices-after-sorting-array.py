# Time:  O(n)

class Solution(object):
    def targetIndices(self, nums, target):
        
        less = sum(x < target for x in nums)
        return list(range(less, less+sum(x == target for x in nums)))
