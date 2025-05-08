# Time:  O(logn),  n is the max of (x, y)

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        return z == 0 or ((z <= x + y) and (z % gcd(x, y) == 0))

