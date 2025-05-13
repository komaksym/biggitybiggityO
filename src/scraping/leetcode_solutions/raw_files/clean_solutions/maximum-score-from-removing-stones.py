# Time:  O(1)

class Solution(object):
    def maximumScore(self, a, b, c):
        return min((a+b+c)//2, a+b+c - max(a, b, c))
