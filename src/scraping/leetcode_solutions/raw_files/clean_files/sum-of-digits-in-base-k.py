# Time:  O(logn)

class Solution(object):
    def sumBase(self, n, k):
        result = 0
        while n:
            n, r = divmod(n, k)
            result += r
        return result
