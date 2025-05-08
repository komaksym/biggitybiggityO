# Time:  O(n + 26)

import itertools


# hash table
class Solution(object):
    def numberOfSpecialChars(self, word):
        lookup1 = [False]*26
        lookup2 = [False]*26
        for x in word:
            if x.islower():
                lookup1[ord(x)-ord('a')] = True
            else:
                lookup2[ord(x)-ord('A')] = True
        return sum(x == y == True for x, y in zip(lookup1, lookup2))
