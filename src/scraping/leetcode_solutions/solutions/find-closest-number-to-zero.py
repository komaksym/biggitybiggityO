# Time:  O(n)

# array
class Solution(object):
    def findClosestNumber(self, nums):
        return max(nums, key=lambda x:(-abs(x), x))
