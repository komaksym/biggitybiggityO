# Time:  cotr:      O(1)
#        push:      O(1)
#        pop:       O(1)
#        increment: O(1)

class CustomStack(object):

    def __init__(self, maxSize):
        self.__max_size = maxSize
        self.__stk = []

    def push(self, x):
        if len(self.__stk) == self.__max_size:
            return
        self.__stk.append([x, 0])

    def pop(self):
        if not self.__stk:
            return -1
        x, inc = self.__stk.pop()
        if self.__stk:
            self.__stk[-1][1] += inc
        return x + inc

    def increment(self, k, val):
        i = min(len(self.__stk), k)-1
        if i >= 0:
            self.__stk[i][1] += val
