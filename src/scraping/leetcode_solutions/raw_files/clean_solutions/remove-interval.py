# Time:  O(n)

class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        A, B = toBeRemoved
        return [[x, y] for a, b in intervals
                for x, y in ((a, min(A, b)), (max(a, B), b))
                if x < y]
