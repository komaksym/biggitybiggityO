# Time:  O(nlogn)

import heapq


# heap, greedy
class Solution(object):
    def minEliminationTime(self, timeReq, splitTime):
        
        heapq.heapify(timeReq)
        for _ in range(len(timeReq)-1):
            heapq.heappush(timeReq, max(heapq.heappop(timeReq), heapq.heappop(timeReq))+splitTime)
        return timeReq[0]
