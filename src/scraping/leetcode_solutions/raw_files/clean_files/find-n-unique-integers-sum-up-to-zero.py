# Time:  O(n)

class Solution(object):
    def sumZero(self, n):
        return [i for i in range(-(n//2), n//2+1) if not (i == 0 and n%2 == 0)]
