# Time:  O(n)

class Solution(object):
    def decompressRLElist(self, nums):
        return [nums[i+1] for i in range(0, len(nums), 2) for _ in range(nums[i])]
