# Time:  O(n)

class Solution(object):
    def smallestEqual(self, nums):
        
        return next((i for i, x in enumerate(nums) if i%10 == x), -1)
