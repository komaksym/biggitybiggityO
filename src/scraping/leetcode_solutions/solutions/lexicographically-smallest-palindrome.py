# Time:  O(n)

# greedy
class Solution(object):
    def makeSmallestPalindrome(self, s):
        return "".join(min(s[i], s[~i]) for i in range(len(s)))
