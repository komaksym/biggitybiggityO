# Time:  ctor: O(1)
#        add : O(1)
#        get : O(1)

class ProductOfNumbers(object):

    def __init__(self):
        self.__accu = [1]

    def add(self, num):
        if not num:
            self.__accu = [1]
            return
        self.__accu.append(self.__accu[-1]*num)             

    def getProduct(self, k):
        if len(self.__accu) <= k:
            return 0
        return self.__accu[-1] // self.__accu[-1-k]
