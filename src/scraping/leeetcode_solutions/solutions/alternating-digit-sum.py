# Time:  O(logn)

# math
class Solution(object):
    def alternateDigitSum(self, n):
        
        result = 0
        sign = 1
        while n:
            sign *= -1
            result += sign*(n%10)
            n //= 10
        return sign*result
