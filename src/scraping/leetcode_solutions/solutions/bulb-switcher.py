# Time:  O(1)
# Space: O(1)

import math


class Solution(object):
    def bulbSwitch(self, n):
        """
        type n: int
        rtype: int
        """
        return int(math.sqrt(n))

