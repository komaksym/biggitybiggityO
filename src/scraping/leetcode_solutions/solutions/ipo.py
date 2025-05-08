# Time:  O(nlogn)

import heapq


class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        
        curr = []
        future = sorted(zip(Capital, Profits), reverse=True)
        for _ in range(k):
            while future and future[-1][0] <= W:
                heapq.heappush(curr, -future.pop()[1])
            if curr:
                W -= heapq.heappop(curr)
        return W

