# Time:  O(m * n)

import itertools


class Solution(object):
    def luckyNumbers (self, matrix):
        rows = list(map(min, matrix))
        cols = list(map(max, zip(*matrix)))
        return [cell for i, row in enumerate(matrix)
                     for j, cell in enumerate(row) if rows[i] == cols[j]]

import itertools


class Solution2(object):
    def luckyNumbers (self, matrix):
        return list(set(map(min, matrix)) &
                    set(map(max, zip(*matrix))))
 
