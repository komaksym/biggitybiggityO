# Time:  O(n)

# array
class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(1, len(pref))):
            pref[i] ^= pref[i-1]
        return pref
