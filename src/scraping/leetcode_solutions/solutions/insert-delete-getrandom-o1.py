# Time:  O(1)

from random import randint

class RandomizedSet(object):

    def __init__(self):
        self.__set = []
        self.__used = {}


    def insert(self, val):
        if val in self.__used:
            return False

        self.__set += val,
        self.__used[val] = len(self.__set)-1

        return True


    def remove(self, val):
        if val not in self.__used:
            return False

        self.__used[self.__set[-1]] = self.__used[val]
        self.__set[self.__used[val]], self.__set[-1] = self.__set[-1], self.__set[self.__used[val]]

        self.__used.pop(val)
        self.__set.pop()

        return True

    def getRandom(self):
        return self.__set[randint(0, len(self.__set)-1)]



