# Time:  ctor:  O(n)
#        query: O(logn)

import collections
import bisect


class RangeFreqQuery(object):

    def __init__(self, arr):
        self.__idxs = collections.defaultdict(list)
        for i, x in enumerate(arr):
            self.__idxs[x].append(i)

    def query(self, left, right, value):
        return bisect.bisect_right(self.__idxs[value], right) - \
               bisect.bisect_left(self.__idxs[value], left)
