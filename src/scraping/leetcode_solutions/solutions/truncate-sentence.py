# Time:  O(n)

class Solution(object):
    def truncateSentence(self, s, k):
        
        for i in range(len(s)):
            if s[i] == ' ':
                k -= 1
                if not k:
                    return s[:i]
        return s
