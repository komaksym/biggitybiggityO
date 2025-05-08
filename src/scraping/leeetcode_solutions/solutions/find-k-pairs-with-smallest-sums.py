# Time:  O(k * log(min(n, m, k))), where n is the size of num1, and m is the size of num2.

from heapq import heappush, heappop

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        
        pairs = []
        if len(nums1) > len(nums2):
            tmp = self.kSmallestPairs(nums2, nums1, k)
            for pair in tmp:
                pairs.append([pair[1], pair[0]])
            return pairs

        min_heap = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(min_heap, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        while min_heap and len(pairs) < k:
            _, i, j = heappop(min_heap)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0) 


# time: O(mn * log k)
from heapq import nsmallest
from itertools import product


class Solution2(object):
    def kSmallestPairs(self, nums1, nums2, k):
        
        return nsmallest(k, product(nums1, nums2), key=sum)
