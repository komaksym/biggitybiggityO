# Time:  O(n)

import collections


class Solution(object):
    def areOccurrencesEqual(self, s):
        return len(set(collections.Counter(s).values())) == 1
