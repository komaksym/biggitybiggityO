# Time:  O(n)

# string
class Solution(object):
    def scoreOfString(self, s):
        
        return sum(abs(ord(s[i+1])-ord(s[i])) for i in range(len(s)-1))
