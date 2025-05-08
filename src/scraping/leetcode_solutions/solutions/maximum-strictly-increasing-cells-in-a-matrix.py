# Time:  O(m * n * log(m * n))

import collections


# sort, dp
class Solution(object):
    def maxIncreasingCells(self, mat):
        lookup = collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                lookup[mat[i][j]].append((i, j))
        dp = [[0]*len(mat[0]) for _ in range(len(mat))]
        row, col = [0]*len(mat), [0]*len(mat[0])
        for x in sorted(lookup.keys()):
            for i, j in lookup[x]:
                dp[i][j] = max(row[i], col[j])+1
            for i, j in lookup[x]:
                row[i] = max(row[i], dp[i][j])
                col[j] = max(col[j], dp[i][j])
        return max(row)
