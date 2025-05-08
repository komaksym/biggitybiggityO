# Time:  O(1)
# Space: O(1)

import math


class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = int((6*n)**(1.0/3))  
        if h*(h+1)*(h+2) > 6*n:
            h -= 1
        n -= h*(h+1)*(h+2)//6
        d = int(math.ceil((-1+(1+8*n)**0.5)/2)) 
        return h*(h+1)//2 + d
