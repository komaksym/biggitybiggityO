# Time:  O(n)

class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+(b-1))//b

        result = prev = 0
        for curr in rungs:
            result += ceil_divide(curr-prev, dist)-1
            prev = curr
        return result
