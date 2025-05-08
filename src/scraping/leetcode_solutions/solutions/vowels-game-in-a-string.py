# Time:  O(n)

# math
class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return any(x in "aeiou" for x in s)
