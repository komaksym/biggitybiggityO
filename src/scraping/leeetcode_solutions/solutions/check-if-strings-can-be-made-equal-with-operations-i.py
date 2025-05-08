# Time:  O(1)

import collections


# freq table
class Solution(object):
    def canBeEqual(self, s1, s2):
        
        return all(collections.Counter(s1[j] for j in range(i, len(s1), 2)) == collections.Counter(s2[j] for j in range(i, len(s2), 2)) for i in range(2))


# Time:  O(1)
# brute force
class Solution2(object):
    def canBeEqual(self, s1, s2):
        
        return (((s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2] and s1[2] == s2[0])) and
                ((s1[1] == s2[1] and s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1])))
