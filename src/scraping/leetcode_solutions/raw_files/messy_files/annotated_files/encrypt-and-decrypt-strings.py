# Time:  ctor:    O(m + d), m is len(keys), d is sum(len(x) for x in dictionary)
#        encrypt: O(n)
#        decrypt: O(n)

import collections
import itertools


# freq table
class Solution(object):

    def __init__(self, keys, values, dictionary):
        self.__lookup = {k: v for k, v in zip(keys, values)}
        self.__cnt = collections.Counter(self.encrypt(x) for x in dictionary)
        
    def encrypt(self, word1):
        if any(c not in self.__lookup for c in word1):
            return ""
        return "".join(self.__lookup[c] for c in word1)

    def decrypt(self, word2):
        return self.__cnt[word2]
