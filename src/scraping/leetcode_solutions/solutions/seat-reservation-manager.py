# Time:  ctor:      O(n)
#        reserve:   O(logn)
#        unreserve: O(logn)
# Space: O(n)

import heapq


class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.__min_heap = list(range(1, n+1))

    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.__min_heap)

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.__min_heap, seatNumber)
