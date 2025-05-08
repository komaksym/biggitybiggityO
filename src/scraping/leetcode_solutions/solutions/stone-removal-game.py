# Time:  O(1)

# math
class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c = 10
        l = int(((2*c+1)-((2*c+1)**2-8*n)**0.5)/2)
        return l%2 == 1
    
