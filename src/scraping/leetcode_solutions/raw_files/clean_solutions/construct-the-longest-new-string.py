# Time:  O(1)

# constructive algorithms, math
class Solution(object):
    def longestString(self, x, y, z):
        return ((min(x, y)*2+int(x != y))+z)*2
