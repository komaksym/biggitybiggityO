# Time:  O(m * n)

# array
class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        return max(([i, mat[i].count(1)] for i in range(len(mat))), key=lambda x: x[1])
