# Time:  O(n)

import collections


class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        lookup = collections.defaultdict(set)
        for u, t in logs:
            lookup[u].add(t)
        result = [0]*k
        for _, ts in lookup.items():
            result[len(ts)-1] += 1
        return result
