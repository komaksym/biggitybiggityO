# Time:  O(nlogk)

import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        
        self.__k = k
        self.__min_heap = []
        for n in nums:
            self.add(n)
        

    def add(self, val):
        
        heapq.heappush(self.__min_heap, val)
        if len(self.__min_heap) > self.__k:
            heapq.heappop(self.__min_heap)
        return self.__min_heap[0]



