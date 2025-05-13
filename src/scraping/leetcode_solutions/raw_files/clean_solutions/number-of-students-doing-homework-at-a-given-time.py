# Time:  O(n)

import itertools


class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
