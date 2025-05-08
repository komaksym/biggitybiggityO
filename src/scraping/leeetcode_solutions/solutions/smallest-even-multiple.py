# Time:  O(1)

# math, bit manipulation
class Solution(object):
    def smallestEvenMultiple(self, n):
        
        return n<<(n&1)
