# Time:  O(n^3)

import collections
import itertools


class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        
        lookup = collections.defaultdict(list)
        A = list(zip(timestamp, username, website))
        A.sort()
        for t, u, w in A:
            lookup[u].append(w)
        count = sum([collections.Counter(set(itertools.combinations(lookup[u], 3))) for u in lookup], collections.Counter())
        return list(min(count, key=lambda x: (-count[x], x)))
