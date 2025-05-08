# Time:  O(n)

# bit manipulation
class Solution(object):
    def minBitwiseArray(self, nums):
        
        return [x-(((x+1)&~x)>>1) if x&1 else -1 for x in nums]

