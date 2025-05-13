# Time:  O(m * n)

# greedy
class Solution(object):
    def minimumOperations(self, grid):
        result = 0
        for i in range(len(grid)-1):
            for j in range(len(grid[0])):
                if grid[i][j]+1 <= grid[i+1][j]:
                    continue
                result += (grid[i][j]+1)-grid[i+1][j]
                grid[i+1][j] = grid[i][j]+1
        return result
