# Time:  O(log(max(m, n)))

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        
        while tx >= sx and ty >= sy:
            if tx < ty:
                sx, sy = sy, sx
                tx, ty = ty, tx
            if ty > sy:
                tx %= ty
            else:
                return (tx - sx) % ty == 0

        return False

