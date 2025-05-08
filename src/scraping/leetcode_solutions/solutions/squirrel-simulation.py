# Time:  O(n)

class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        result = 0
        d = float("inf")
        for nut in nuts:
            result += (distance(nut, tree) * 2)
            d = min(d, distance(nut, squirrel) - distance(nut, tree))
        return result + d

