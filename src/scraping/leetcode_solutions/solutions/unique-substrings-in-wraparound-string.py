# Time:  O(n)

class Solution(object):
    def findSubstringInWraproundString(self, p):
        
        letters = [0] * 26
        result, length = 0, 0
        for i in range(len(p)):
            curr = ord(p[i]) - ord('a')
            if i > 0 and ord(p[i-1]) != (curr-1)%26 + ord('a'):
                length = 0
            length += 1
            if length > letters[curr]:
                result += length - letters[curr]
                letters[curr] = length
        return result

