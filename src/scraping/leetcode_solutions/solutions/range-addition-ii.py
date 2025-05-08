# Time:  O(p), p is the number of ops

class Solution(object):
    def maxCount(self, m, n, ops):
        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])
        return m*n

