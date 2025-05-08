# Time:  O(nlogn)

import itertools


class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        sorted_x = sorted({x for x, y in points})
        return max([b-a for a, b in zip(sorted_x, sorted_x[1:])] + [0])
