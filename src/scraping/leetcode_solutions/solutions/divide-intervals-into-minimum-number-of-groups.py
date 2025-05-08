# Time:  O(nlogn)

import collections


# sort, line sweep
class Solution(object):
    def minGroups(self, intervals):
        events = collections.Counter()
        for l, r in intervals:
            events[l] += 1
            events[r+1] -= 1
        result = curr = 0
        for t in sorted(events.keys()):
            curr += events[t]
            result = max(result, curr)
        return result
