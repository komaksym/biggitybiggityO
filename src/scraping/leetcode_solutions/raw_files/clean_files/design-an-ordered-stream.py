# Time:  O(1), amortized

class Solution(object):

    def __init__(self, n):
        self.__i = 0      
        self.__values = [None]*n

    def insert(self, id, value):
        id -= 1
        self.__values[id] = value
        result = []
        if self.__i != id:
            return result
        while self.__i < len(self.__values) and self.__values[self.__i]:
            result.append(self.__values[self.__i])
            self.__i += 1
        return result
