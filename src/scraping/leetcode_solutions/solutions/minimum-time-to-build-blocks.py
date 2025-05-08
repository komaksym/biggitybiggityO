# Time:  O(nlogn)

import heapq


class Solution(object):
    def minBuildTime(self, blocks, split):
        heapq.heapify(blocks)
        while len(blocks) != 1:
            x, y = heapq.heappop(blocks), heapq.heappop(blocks)
            heapq.heappush(blocks, y+split)
        return heapq.heappop(blocks)
