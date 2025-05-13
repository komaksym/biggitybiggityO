# Time:  O(logn)

import math


class Solution(object):
    def arrangeCoins(self, n):
        return int((math.sqrt(8*n+1)-1) / 2) 


# Time:  O(logn)
class Solution2(object):
    def arrangeCoins(self, n):
        def check(mid, n):
            return mid*(mid+1) <= 2*n

        left, right = 1, n
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid, n):
                right = mid-1
            else:
                left = mid+1
        return right
