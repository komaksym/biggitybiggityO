# Time:  O(n)

import itertools


class Solution(object):
    def printVertically(self, s):
        
        return ["".join(c).rstrip() for c in itertools.zip_longest(*s.split(), fillvalue=' ')]
