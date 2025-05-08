# Time:  O(n)

# array
class Solution(object):
    def findArray(self, pref):
        for i in reversed(range(1, len(pref))):
            pref[i] ^= pref[i-1]
        return pref
