from functools import reduce
# Time:  O(n)

# bit manipulation
class Solution(object):
    def maximumXOR(self, nums):
        
        return reduce(lambda x, y: x|y, nums)
