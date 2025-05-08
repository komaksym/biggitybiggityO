# Time:  O(m * n)
# Space: O(n)

class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        intersections = set(mat[0])
        for i in range(1, len(mat)):
            intersections &= set(mat[i])
            if not intersections:
                return -1
        return min(intersections)


# Time:  O(m * n)
# Space: O(n)
import collections


class Solution2(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        counter = collections.Counter()
        for row in mat:
            for c in row:
                counter[c] += 1
                if counter[c] == len(mat):
                    return c
        return -1
