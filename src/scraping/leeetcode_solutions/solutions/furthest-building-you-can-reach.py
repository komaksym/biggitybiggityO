# Time:  O(nlogk)

import heapq


class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        
        min_heap = []
        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff > 0:
                heapq.heappush(min_heap, diff)
            if len(min_heap) <= ladders: 
                continue
            bricks -= heapq.heappop(min_heap) 
            if bricks < 0: 
                return i
        return len(heights)-1
