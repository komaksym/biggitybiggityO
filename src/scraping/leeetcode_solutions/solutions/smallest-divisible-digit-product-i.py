# Time:  O(logn)

# brute force
class Solution(object):
    def smallestNumber(self, n, t):
        
        def check(x):
            result = 1
            while x:
                result = (result*(x%10))%t
                x //= 10
            return result == 0
    
        while not check(n):
            n += 1
        return n
