# Time:  O(n^2 * logn)

# sort
class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        lookup = [[] for _ in range((len(grid)-1)+(len(grid[0])-1)-(0-(len(grid[0])-1))+1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                lookup[i-j].append(grid[i][j])
        for i in range(0-(len(grid[0])-1), (len(grid)-1)+(len(grid[0])-1)+1):
            if i < 0:
                lookup[i].sort(reverse=True)
            else:
                lookup[i].sort()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = lookup[i-j].pop()
        return grid
