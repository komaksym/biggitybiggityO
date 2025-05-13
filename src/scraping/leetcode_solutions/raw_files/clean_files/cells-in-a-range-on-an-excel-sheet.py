# Time:  O(26^2)

# enumeration
class Solution(object):
    def cellsInRange(self, s):
        return [chr(x)+chr(y) for x in range(ord(s[0]), ord(s[3])+1) for y in range(ord(s[1]), ord(s[4])+1)]
