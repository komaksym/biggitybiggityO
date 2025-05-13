# Time:  ctor: O(n)
#        q:    O(logn)

import collections
import itertools
import bisect


class Solution(object):

    def __init__(self, persons, times):
        lead = -1
        self.__lookup, count = [], collections.defaultdict(int)
        for t, p in zip(times, persons):
            count[p] += 1
            if count[p] >= count[lead]:
                lead = p
                self.__lookup.append((t, lead))

    def q(self, t):
        return self.__lookup[bisect.bisect(self.__lookup,
                                           (t, float("inf")))-1][1]



