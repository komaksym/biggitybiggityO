# Time:  O(n)

# array
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        
        return max((l**2+w**2, l*w) for l, w in dimensions)[1]
