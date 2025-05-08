# Time:  O(n)

import collections


# freq table
class Solution(object):
    def checkStrings(self, s1, s2):
        
        return all(collections.Counter(s1[j] for j in range(i, len(s1), 2)) == collections.Counter(s2[j] for j in range(i, len(s2), 2)) for i in range(2))
