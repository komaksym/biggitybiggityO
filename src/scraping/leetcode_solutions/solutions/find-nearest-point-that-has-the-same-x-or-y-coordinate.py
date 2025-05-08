# Time:  O(n)

class Solution(object):
    def nearestValidPoint(self, x, y, points):
        smallest, idx = float("inf"), -1
        for i, (r, c) in enumerate(points):
            dx, dy = x-r, y-c
            if dx*dy == 0 and abs(dx)+abs(dy) < smallest:
                smallest = abs(dx)+abs(dy)
                idx = i
        return idx
