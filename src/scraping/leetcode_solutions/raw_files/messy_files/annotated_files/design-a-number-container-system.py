# Time:  ctor:   O(1)
#        change: O(logn)
#        find:   O(1)

from sortedcontainers import SortedList


# sorted list
class Solution(object):

    def __init__(self):
        self.__idx_to_num = {}
        self.__num_to_idxs = collections.defaultdict(SortedList)

    def change(self, index, number):
        if index in self.__idx_to_num:
            self.__num_to_idxs[self.__idx_to_num[index]].remove(index)
            if not self.__num_to_idxs[self.__idx_to_num[index]]:
                del self.__num_to_idxs[self.__idx_to_num[index]]
        self.__idx_to_num[index] = number
        self.__num_to_idxs[number].add(index)

    def find(self, number):
        return self.__num_to_idxs[number][0] if number in self.__num_to_idxs else -1
