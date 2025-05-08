# Time:  O(n * l)

import itertools


# string
class Solution(object):
    def countPrefixes(self, words, s):
        return sum(map(s.startswith, words))
