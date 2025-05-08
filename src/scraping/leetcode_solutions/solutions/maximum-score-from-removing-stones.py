# Time:  O(1)

class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        return min((a+b+c)//2, a+b+c - max(a, b, c))
