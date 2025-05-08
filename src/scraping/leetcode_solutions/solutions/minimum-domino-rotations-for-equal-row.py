# Time:  O(n)

import itertools
from functools import reduce


class Solution(object):
    def minDominoRotations(self, A, B):
        intersect = reduce(set.__and__, [set(d) for d in zip(A, B)])
        if not intersect:
            return -1
        x = intersect.pop()
        return min(len(A)-A.count(x), len(B)-B.count(x))
