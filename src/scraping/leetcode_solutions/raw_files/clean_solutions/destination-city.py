# Time:  O(n)

import itertools


class Solution(object):
    def destCity(self, paths):
        A, B = list(map(set, zip(*paths)))
        return (B-A).pop()
