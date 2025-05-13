# Time:  O(1)

# bit manipulation
class Solution(object):
    def maxNumber(self, n):
        return (1<<(n.bit_length()-1))-1
