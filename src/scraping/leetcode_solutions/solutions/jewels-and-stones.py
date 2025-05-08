# Time:  O(m + n)

class Solution(object):
    def numJewelsInStones(self, J, S):
        
        lookup = set(J)
        return sum(s in lookup for s in S)


