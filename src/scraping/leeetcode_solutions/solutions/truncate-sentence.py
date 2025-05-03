# Time:  O(n)
# Space: O(1)

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for i in range(len(s)):
            if s[i] == ' ':
                k -= 1
                if not k:
                    return s[:i]
        return s
