# Time:  O(1)

import collections


class FrontMiddleBackQueue(object):

    def __init__(self):
        self.__left, self.__right = collections.deque(), collections.deque()   

    def pushFront(self, val):
        self.__left.appendleft(val)
        self.__balance()        

    def pushMiddle(self, val):
        if len(self.__left) > len(self.__right):
            self.__right.appendleft(self.__left.pop())
        self.__left.append(val)

    def pushBack(self, val):
        self.__right.append(val)
        self.__balance()

    def popFront(self):
        val = (self.__left or collections.deque([-1])).popleft()
        self.__balance()
        return val

    def popMiddle(self):
        val = (self.__left or [-1]).pop()
        self.__balance()
        return val

    def popBack(self):
        val = (self.__right or self.__left or [-1]).pop()
        self.__balance()
        return val

    def __balance(self):
        if len(self.__left) > len(self.__right)+1:
            self.__right.appendleft(self.__left.pop())
        elif len(self.__left) < len(self.__right):
            self.__left.append(self.__right.popleft())
