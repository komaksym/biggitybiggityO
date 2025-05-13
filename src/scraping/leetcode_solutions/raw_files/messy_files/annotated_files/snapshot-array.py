# Time:  set: O(1)
#        get: O(logn), n is the total number of set

import collections
import bisect


class Solution(object):

    def __init__(self, length):
        self.__A = collections.defaultdict(lambda: [[0, 0]])
        self.__snap_id = 0


    def set(self, index, val):
        if self.__A[index][-1][0] == self.__snap_id:
            self.__A[index][-1][1] = val
        else:
            self.__A[index].append([self.__snap_id, val])


    def snap(self):
        self.__snap_id += 1
        return self.__snap_id - 1


    def get(self, index, snap_id):
        i = bisect.bisect_left(self.__A[index], [snap_id+1, float("-inf")]) - 1
        return self.__A[index][i][1]   
