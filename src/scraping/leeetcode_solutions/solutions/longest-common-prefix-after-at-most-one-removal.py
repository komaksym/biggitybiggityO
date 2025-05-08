# Time:  O(n)

# two pointers
class Solution(object):
    def longestCommonPrefix(self, s, t):
        
        result = i = j = 0
        removed = False
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                result += 1
                i += 1
                j += 1
            elif not removed:
                removed = True
                i += 1
            else:
                break
        return result
