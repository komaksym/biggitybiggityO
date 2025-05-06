# Time:  O(m * n)

# array
class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        return all(row[i] == row[(i+k)%len(row)]for row in mat for i in range(len(row)))
