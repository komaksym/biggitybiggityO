# Time:  ctor:   O(m * n),
#        lookup: O(1)

class Solution(object):
    def __init__(self, matrix):
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        self.__sums = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.__sums[i][j] = self.__sums[i][j-1] + self.__sums[i-1][j] - \
                                    self.__sums[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        return self.__sums[row2+1][col2+1] - self.__sums[row2+1][col1] - \
               self.__sums[row1][col2+1] + self.__sums[row1][col1]



