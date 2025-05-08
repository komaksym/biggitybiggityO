# Time:  O(q + nlogn)

# hash table, heap
class Solution(object):
    def unmarkedSumArray(self, nums, queries):
        total = sum(nums)
        lookup = [False]*len(nums)
        min_heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(min_heap)
        result = []
        for i, k in queries:
            if not lookup[i]:
                lookup[i] = True
                total -= nums[i]
            for _ in range(k):
                while min_heap:
                    x, i = heapq.heappop(min_heap)
                    if lookup[i]:
                        continue
                    lookup[i] = True
                    total -= x
                    break
                if not min_heap:
                    break
            result.append(total)
        return result
