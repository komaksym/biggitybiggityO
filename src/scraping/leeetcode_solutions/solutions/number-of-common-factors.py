# Time:  O(log(min(a, b)) + sqrt(gcd))

# math
class Solution(object):
    def commonFactors(self, a, b):
        
        def gcd(a, b): 
            while b:
                a, b = b, a%b
            return a
        
        g = gcd(a, b)
        result = 0
        x = 1
        while x*x <= g:
            if g%x == 0:
                result += 1 if g//x == x else 2
            x += 1
        return result
