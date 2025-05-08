# Time:  O(m * n)

# array
class Solution(object):
    def rowAndMaximumOnes(self, mat):
        
        return max(([i, mat[i].count(1)] for i in range(len(mat))), key=lambda x: x[1])
