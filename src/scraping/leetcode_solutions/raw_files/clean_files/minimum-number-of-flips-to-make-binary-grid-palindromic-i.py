# Time:  O(m * n)

# array, greedy
class Solution(object):
    def minFlips(self, grid):
        def count(m, n, get):
            return sum(get(i, j) != get(i, ~j) for i in range(m) for j in range(n//2))

        m, n = len(grid), len(grid[0])
        return min(count(m, n, lambda i, j: grid[i][j]),
                   count(n, m, lambda i, j: grid[j][i]))
