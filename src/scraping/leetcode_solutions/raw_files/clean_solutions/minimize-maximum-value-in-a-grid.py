# Time:  O((m * n) * log(m * n))

# sort, greedy
class Solution(object):
    def minScore(self, grid):
        idxs = [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        idxs.sort(key=lambda x: grid[x[0]][x[1]])
        row_max, col_max = [0]*len(grid), [0]*len(grid[0])
        for i, j in idxs:
            grid[i][j] = row_max[i] = col_max[j] = max(row_max[i], col_max[j])+1
        return grid
