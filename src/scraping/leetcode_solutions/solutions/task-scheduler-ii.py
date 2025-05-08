# Time:  O(n)

import collections


# hash table
class Solution(object):
    def taskSchedulerII(self, tasks, space):
        lookup = collections.defaultdict(int)
        result = 0
        for t in tasks:
            result = max(lookup[t], result+1)
            lookup[t] = result+space+1
        return result
