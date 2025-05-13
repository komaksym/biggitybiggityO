# Time:  O(n)

class Solution(object):
    def titleToNumber(self, s):
        result = 0
        for i in range(len(s)):
            result *= 26
            result += ord(s[i]) - ord('A') + 1
        return result


