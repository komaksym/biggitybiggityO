# Time:  O(n * m)

# prefix sum
class Solution(object):
    def countSubmatrices(self, grid, k):
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i-1 >= 0:
                    grid[i][j] += grid[i-1][j]
                if j-1 >= 0:
                    grid[i][j] += grid[i][j-1]
                if i-1 >= 0 and j-1 >= 0:
                    grid[i][j] -= grid[i-1][j-1]
                if grid[i][j] <= k:
                    result += 1
        return result
