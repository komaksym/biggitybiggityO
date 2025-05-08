# Time:  O(n)

# two pointers
class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        
        result = left = prev = 0
        for right in range(len(s)):
            if right-1 >= 0 and s[right-1] == s[right]:
                left, prev = prev, right
            result = max(result, right-left+1)
        return result
