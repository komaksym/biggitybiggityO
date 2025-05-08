# Time:  O(m * n)

class Solution(object):
    def smallestCommonElement(self, mat):
        
       
        intersections = set(mat[0])
        for i in range(1, len(mat)):
            intersections &= set(mat[i])
            if not intersections:
                return -1
        return min(intersections)


# Time:  O(m * n)
import collections


class Solution2(object):
    def smallestCommonElement(self, mat):
        
       
        counter = collections.Counter()
        for row in mat:
            for c in row:
                counter[c] += 1
                if counter[c] == len(mat):
                    return c
        return -1
