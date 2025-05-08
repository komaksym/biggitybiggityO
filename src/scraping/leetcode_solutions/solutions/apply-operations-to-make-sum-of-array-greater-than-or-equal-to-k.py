# Time:  O(logn)

# math
class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        def isqrt(n):
            a, b = n, (n+1)//2
            while b < a:
                a, b = b, (b+n//b)//2
            return a

        def ceil_divide(a, b):
            return (a+b-1)//b
    
        x = isqrt(k)
        return (x-1)+(ceil_divide(k, x)-1)
