# Time:  ctor:    O(1)
#        upload:  O(1), amortized
#        longest: O(1)

# hash table
class Solution(object):

    def __init__(self, n):
        self.__lookup = set()
        self.__curr = 0

    def upload(self, video):
        self.__lookup.add(video-1)
        while self.__curr in self.__lookup:
            self.__lookup.remove(self.__curr)
            self.__curr += 1

    def longest(self):
        return self.__curr
