# Time:  O(1)

# constructive algorithms, math
class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        diff1, diff2 = abs(sx-fx), abs(sy-fy)
        mn = min(diff1, diff2)+abs(diff1-diff2)
        return t >= mn if mn else t != 1
