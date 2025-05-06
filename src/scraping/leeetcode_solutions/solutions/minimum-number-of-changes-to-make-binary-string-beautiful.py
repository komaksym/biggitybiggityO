# Time:  O(n)

# greedy
class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(s[i] != s[i+1] for i in range(0, len(s), 2))
