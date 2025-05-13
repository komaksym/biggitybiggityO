# Time:  O(1)

from random import randint
from collections import defaultdict

class Solution(object):

    def __init__(self):
        self.__list = []
        self.__used = defaultdict(list)


    def insert(self, val):
        has = val in self.__used

        self.__list += (val, len(self.__used[val])),
        self.__used[val] += len(self.__list)-1,

        return not has


    def remove(self, val):
        if val not in self.__used:
            return False

        self.__used[self.__list[-1][0]][self.__list[-1][1]] = self.__used[val][-1]
        self.__list[self.__used[val][-1]], self.__list[-1] = self.__list[-1], self.__list[self.__used[val][-1]]

        self.__used[val].pop()
        if not self.__used[val]:
            self.__used.pop(val)
        self.__list.pop()

        return True

    def getRandom(self):
        return self.__list[randint(0, len(self.__list)-1)][0]
