# Time:  O(m * n)

class Solution(object):
    def construct2DArray(self, original, m, n):
        
        return [original[i:i+n] for i in range(0, len(original), n)] if len(original) == m*n else []
