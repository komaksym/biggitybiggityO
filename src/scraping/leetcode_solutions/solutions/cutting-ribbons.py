from functools import reduce
# Time:  O(nlogr), r is sum(ribbons)/k

class Solution(object):
    def maxLength(self, ribbons, k):
        def check(ribbons, k, s):
            return reduce(lambda total,x: total+x//s, ribbons, 0) >= k

        left, right = 1, sum(ribbons)//k
        while left <= right:
            mid = left + (right-left)//2
            if not check(ribbons, k, mid):
                right = mid-1
            else:
                left = mid+1
        return right
