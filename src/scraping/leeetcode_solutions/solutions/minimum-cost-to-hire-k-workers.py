# Time:   O(nlogn)

import itertools
import heapq


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        
        result, qsum = float("inf"), 0
        max_heap = []
        for r, q in sorted([float(w)/q, q] for w, q in zip(wage, quality)):
            qsum += q
            heapq.heappush(max_heap, -q)
            if len(max_heap) > K:
                qsum -= -heapq.heappop(max_heap)
            if len(max_heap) == K:
                result = min(result, qsum*r)
        return result

