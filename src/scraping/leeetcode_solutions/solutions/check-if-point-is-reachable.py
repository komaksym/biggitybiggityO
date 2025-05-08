# Time:  O(log(min(a, b)))

# number theory
class Solution(object):
    def isReachable(self, targetX, targetY):
        
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
    
        g = gcd(targetX, targetY)
        return g == (g&~(g-1)) 
