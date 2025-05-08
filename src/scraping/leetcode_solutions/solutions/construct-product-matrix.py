# Time:  O(m * n)

# prefix sum
class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        right = [1]*(len(grid)*len(grid[0])+1)
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                right[i*len(grid[0])+j] = (right[(i*len(grid[0])+j)+1]*grid[i][j])%MOD
        left = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j], left = (left*right[(i*len(grid[0])+j)+1])%MOD, (left*grid[i][j])%MOD
        return grid


# Time:  O(m * n)
# prefix sum
class Solution2(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        left = [1]*(len(grid)*len(grid[0])+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                left[(i*len(grid[0])+j)+1] = (left[i*len(grid[0])+j]*grid[i][j])%MOD
        right = [1]*(len(grid)*len(grid[0])+1)
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                right[i*len(grid[0])+j] = (right[(i*len(grid[0])+j)+1]*grid[i][j])%MOD
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = (left[i*len(grid[0])+j]*right[(i*len(grid[0])+j)+1])%MOD
        return grid
