# Time:  add: O(logn)
#        get: O(logn)

from sortedcontainers import SortedList


class SORTracker(object):

    def __init__(self):
        self.__sl = SortedList()
        self.__i = 0

    def add(self, name, score):
        
        self.__sl.add((-score, name))
        
    def get(self):
        
        self.__i += 1
        return self.__sl[self.__i-1][1]
