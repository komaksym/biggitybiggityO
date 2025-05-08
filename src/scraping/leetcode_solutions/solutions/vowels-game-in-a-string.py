# Time:  O(n)

# math
class Solution(object):
    def doesAliceWin(self, s):
        
        return any(x in "aeiou" for x in s)
