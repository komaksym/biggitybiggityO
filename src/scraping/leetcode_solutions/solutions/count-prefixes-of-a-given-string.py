# Time:  O(n * l)

import itertools


# string
class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        return sum(map(s.startswith, words))
