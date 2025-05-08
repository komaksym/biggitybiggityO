# Time:  O(1)

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        return 2 if (p & -p) > (q & -q) else 0 if (p & -p) < (q & -q) else 1


# Time:  O(log(max(p, q))) = O(1) due to 32-bit integer
class Solution2(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        lcm = p*q // gcd(p, q)
        if lcm // p % 2 == 1:
            if lcm // q % 2 == 1:
                return 1 
            return 2 
        return 0 

