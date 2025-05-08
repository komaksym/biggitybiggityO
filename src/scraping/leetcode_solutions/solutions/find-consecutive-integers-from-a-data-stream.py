# Time:  O(1)

# array
class DataStream(object):

    def __init__(self, value, k):
        
        self.__value = value
        self.__k = k
        self.__cnt = 0

    def consec(self, num):
        
        if num == self.__value:
            self.__cnt += 1
        else:
            self.__cnt = 0
        return self.__cnt >= self.__k
