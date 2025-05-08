# Time:  O(n * p)

# string
class Solution(object):
    def prefixCount(self, words, pref):
        return sum(x.startswith(pref) for x in words)
