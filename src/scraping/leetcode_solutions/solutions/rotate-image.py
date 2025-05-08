# Time:  O(n^2)

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

        for i in range(n / 2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

        return matrix

# Time:  O(n^2)
class Solution2(object):
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]

