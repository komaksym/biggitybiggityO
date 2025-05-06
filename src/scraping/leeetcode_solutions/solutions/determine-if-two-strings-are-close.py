# Time:  O(n)

import collections


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False 
        
        cnt1, cnt2 = collections.Counter(word1), collections.Counter(word2)   # Reuse of keys
        return set(cnt1.keys()) == set(cnt2.keys()) and \
               collections.Counter(iter(cnt1.values())) == collections.Counter(iter(cnt2.values()))
