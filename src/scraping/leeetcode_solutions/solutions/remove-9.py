# Time:  O(logn)

class Solution(object):
    def newInteger(self, n):
        
        result, base = 0, 1
        while n > 0:
            result += (n%9) * base
            n /= 9
            base *= 10
        return result

