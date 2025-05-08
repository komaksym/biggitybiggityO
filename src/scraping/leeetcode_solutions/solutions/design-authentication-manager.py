# Time:  ctor:     O(1)
#        generate: O(1), amortized
#        renew:    O(1), amortized
#        count:    O(1), amortized

import collections


class AuthenticationManager(object):

    def __init__(self, timeToLive):
        
        self.__time = timeToLive
        self.__lookup = collections.OrderedDict()

    def __evict(self, currentTime):
        while self.__lookup and next(iter(self.__lookup.values())) <= currentTime:
            self.__lookup.popitem(last=False)

    def generate(self, tokenId, currentTime):
        
        self.__evict(currentTime)
        self.__lookup[tokenId] = currentTime + self.__time


    def renew(self, tokenId, currentTime):
        
        self.__evict(currentTime)            
        if tokenId not in self.__lookup:
            return
        del self.__lookup[tokenId]
        self.__lookup[tokenId] = currentTime + self.__time

    def countUnexpiredTokens(self, currentTime):
        
        self.__evict(currentTime)
        return len(self.__lookup)
