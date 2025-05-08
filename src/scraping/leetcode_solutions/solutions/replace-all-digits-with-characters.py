# Time:  O(n)

class Solution(object):
    def replaceDigits(self, s):
        
        return "".join(chr(ord(s[i-1])+int(s[i])) if i%2 else s[i] for i in range(len(s)))
