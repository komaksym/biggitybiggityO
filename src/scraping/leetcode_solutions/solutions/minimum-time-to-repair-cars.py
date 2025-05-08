# Time:  O(mx * log(mn * c^2)) = O(mx * (logc + log(mn))), c = cars, mx = max(ranks), mn = min(ranks)

import collections


# freq table, binary search
class Solution(object):
    def repairCars(self, ranks, cars):
        
        def check(x):
            return sum(int((x//k)**0.5)*v for k, v in cnt.items()) >= cars

        cnt = collections.Counter(ranks)
        left, right = 1, min(cnt.keys())*cars**2
        while left <= right:
            mid = left+(right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left


# Time:  O(c * log(mx)), c = cars, mx = max(ranks)
import collections
import heapq


# freq table, heap, simulation
class Solution2(object):
    def repairCars(self, ranks, cars):
        
        cnt = collections.Counter(ranks)
        min_heap = [(r*1**2, 1) for r in cnt.keys()]
        heapq.heapify(min_heap)
        while cars > 0:
            t, k = heapq.heappop(min_heap)
            r = t//k**2
            cars -= cnt[r]
            k += 1
            heapq.heappush(min_heap, (r*k**2, k))
        return t
