# Time:  O(1)

import math


class Solution(object):
    def constructRectangle(self, area):
        w = int(math.sqrt(area))
        while area % w:
            w -= 1
        return [area // w, w]

