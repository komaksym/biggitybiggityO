# Time:  O(n)

import threading


class Solution(object):
    def __init__(self, n):
        self.__n = n
        self.__curr = False
        self.__cv = threading.Condition()

    def foo(self, printFoo):
        for i in range(self.__n):
            with self.__cv:
                while self.__curr != False:
                    self.__cv.wait()
                self.__curr = not self.__curr
                printFoo()
                self.__cv.notify()

    def bar(self, printBar):
        for i in range(self.__n):
            with self.__cv:
                while self.__curr != True:
                        self.__cv.wait()
                self.__curr = not self.__curr
                printBar()
                self.__cv.notify()
