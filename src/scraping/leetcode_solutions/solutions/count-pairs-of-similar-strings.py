# Time:  O(n * l)

import collections
import itertools
from functools import reduce


# freq table, bitmask
class Solution(object):
    def similarPairs(self, words):
        cnt = collections.Counter()
        result = 0
        for w in words:
            mask = reduce(lambda total, x: total|x, map(lambda c: 1<<(ord(c)-ord('a')), w))
            result += cnt[mask]
            cnt[mask] += 1
        return result
