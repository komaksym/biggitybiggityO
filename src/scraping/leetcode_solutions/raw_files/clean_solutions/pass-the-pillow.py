# Time:  O(1)

# math
class Solution(object):
    def passThePillow(self, n, time):
        return n-abs((n-1)-(time%(2*(n-1))))
