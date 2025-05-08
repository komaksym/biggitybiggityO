# Time:  O(sqrt(c) * logc)

import math


class Solution(object):
    def judgeSquareSum(self, c):
        
        for a in range(int(math.sqrt(c))+1):
            b = int(math.sqrt(c-a**2))
            if a**2 + b**2 == c:
                return True
        return False

