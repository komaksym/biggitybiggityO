# Time:  O(logn)

# bit manipulation, math
class Solution(object):
    def uniqueXorTriplets(self, nums):
        
        return 1<<len(nums).bit_length() if len(nums) >= 3 else len(nums)
