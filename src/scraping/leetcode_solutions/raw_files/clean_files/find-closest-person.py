# Time:  O(1)

# math
class Solution(object):
    def findClosest(self, x, y, z):
        return list(range(3))[cmp(abs(y-z), abs(x-z))]
