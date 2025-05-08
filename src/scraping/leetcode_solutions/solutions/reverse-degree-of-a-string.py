# Time:  O(n)

# string
class Solution(object):
    def reverseDegree(self, s):
        return sum(i*(26-(ord(x)-ord('a'))) for i, x in enumerate(s, 1))
