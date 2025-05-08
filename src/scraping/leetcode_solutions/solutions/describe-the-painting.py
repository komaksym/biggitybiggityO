# Time:  O(nlogn)

import collections


class Solution(object):
    def splitPainting(self, segments):
        
        counts = collections.defaultdict(int)
        for s, e, c in segments:
            counts[s] += c
            counts[e] -= c
        points = sorted(x for x in counts.items())

        result = []
        overlap = prev = 0
        for curr, cnt in points:
            if overlap:
                result.append([prev, curr, overlap])
            overlap += cnt
            prev = curr
        return result
