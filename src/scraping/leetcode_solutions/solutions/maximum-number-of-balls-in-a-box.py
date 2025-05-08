# Time:  O(nlogm)
# Space: O(logm)

import collections
import itertools


class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        count = collections.Counter()
        for i in range(lowLimit, highLimit+1):
            count[sum(map(int, str(i)))] += 1
        return max(count.values())
