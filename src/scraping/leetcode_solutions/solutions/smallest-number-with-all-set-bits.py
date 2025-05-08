# Time:  O(1)

# bit manipulation
class Solution(object):
    def smallestNumber(self, n):
        
        return (1<<n.bit_length())-1
