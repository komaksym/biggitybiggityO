# Time:  O(1)

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ra, ia = list(map(int, a[:-1].split('+')))
        rb, ib = list(map(int, b[:-1].split('+')))
        return '%d+%di' % (ra * rb - ia * ib, ra * ib + ia * rb)

