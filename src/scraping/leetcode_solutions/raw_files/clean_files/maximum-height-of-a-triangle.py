# Time:  O(logn)

# math
class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        def f(x, y):
            a, b = int(2*x**0.5)-1, int((4*y+1)**0.5)-1
            return min(a, b)+int(a != b)
        
        return max(f(red, blue), f(blue, red))


# Time:  O(sqrt(n))
# simulation
class Solution2(object):
    def maxHeightOfTriangle(self, red, blue):
        def f(x, y):
            h = 0
            while x >= h+1:
                h += 1
                x -= h
                x, y = y, x
            return h

        return max(f(red, blue), f(blue, red))
