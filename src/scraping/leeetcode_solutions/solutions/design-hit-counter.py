# Time:  O(1), amortized

from collections import deque

class HitCounter(object):

    def __init__(self):
        
        self.__k = 300
        self.__dq = deque()
        self.__count = 0

    def hit(self, timestamp):
        
        self.getHits(timestamp)
        if self.__dq and self.__dq[-1][0] == timestamp:
            self.__dq[-1][1] += 1
        else:
            self.__dq.append([timestamp, 1])
        self.__count += 1

    def getHits(self, timestamp):
        
        while self.__dq and self.__dq[0][0] <= timestamp - self.__k:
            self.__count -= self.__dq.popleft()[1]
        return self.__count


