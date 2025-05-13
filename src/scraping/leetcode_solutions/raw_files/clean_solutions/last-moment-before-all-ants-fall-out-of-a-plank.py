# Time:  O(n)

class Solution(object):
    def getLastMoment(self, n, left, right):
        return max(max(left or [0]), n-min(right or [n]))
