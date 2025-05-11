# Time:  O(m * n * log(min(m, n))

import collections


class Solution(object):
    def diagonalSort(self, mat):
        lookup = collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                lookup[i-j].append(mat[i][j])
        for v in lookup.values():
            v.sort()
        for i in reversed(range(len(mat))):
            for j in reversed(range(len(mat[0]))):
                mat[i][j] = lookup[i-j].pop()
        return mat
