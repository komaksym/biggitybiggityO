# Time:  O(n^2)

# array
class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        cnt = [[0]*3 for _ in range(2)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cnt[(i <= (len(grid[0])-1)//2 and (i-j == 0 or i+j == len(grid[0])-1)) or (i > (len(grid[0])-1)//2 == j)][grid[i][j]] += 1
        return len(grid)*len(grid[0])-max(cnt[0][i]+cnt[1][j] for i in range(3) for j in range(3) if i != j)
