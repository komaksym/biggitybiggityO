# Time:  O(n)

import threading
import collections


class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        
        self.__cv = threading.Condition()
        self.__q = collections.deque()
        self.__cap = capacity

    def enqueue(self, element):
        
        with self.__cv:
            while len(self.__q) == self.__cap:
                self.__cv.wait()
            self.__q.append(element)
            self.__cv.notifyAll()

    def dequeue(self):
        
        with self.__cv:
            while not self.__q:
                self.__cv.wait()
            self.__cv.notifyAll()
            return self.__q.popleft()

    def size(self):
        
        with self.__cv:
            return len(self.__q)
