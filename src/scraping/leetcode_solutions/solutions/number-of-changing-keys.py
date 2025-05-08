# Time:  O(n)

# string
class Solution(object):
    def countKeyChanges(self, s):
        return sum(s[i].lower() != s[i+1].lower() for i in range(len(s)-1))
