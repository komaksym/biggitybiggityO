# Time:  ctor: O(k)
#        add: O(1)
#        showFirstUnique: O(1)

import collections


class FirstUnique(object):

    def __init__(self, nums):
        
        self.__q = collections.OrderedDict()
        self.__dup = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        
        if self.__q:
            return next(iter(self.__q))
        return -1
    
    def add(self, value):
        
        if value not in self.__dup and value not in self.__q:
            self.__q[value] = None
            return
        if value in self.__q:
            self.__q.pop(value)
            self.__dup.add(value)

