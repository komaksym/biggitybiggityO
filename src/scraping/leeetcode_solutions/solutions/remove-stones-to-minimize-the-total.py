# Time:  O(n + klogn)

import heapq


class Solution(object):
    def minStoneSum(self, piles, k):
        
        for i, x in enumerate(piles):
            piles[i] = -x
        heapq.heapify(piles)
        for i in range(k):
            heapq.heappush(piles, heapq.heappop(piles)//2)
        return -sum(piles)
