# Time:  O(log(max(t)) * logn)

import heapq


class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        total = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)
        while total != len(target):
            y = -heapq.heappop(max_heap)
            remain = total-y
            x = y-remain
            if x <= 0:
                return False
            if x > remain:  # for case [1, 1000000000]
                x = x%remain + remain
            heapq.heappush(max_heap, -x)
            total = x+remain
        return True
