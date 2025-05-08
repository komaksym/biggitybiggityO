# Time:  O(n * p)

# string
class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        return sum(x.startswith(pref) for x in words)
