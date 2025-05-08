# Time:  O(n^2)

# bit manipulation
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        
        n = len(grid)
        a_xor_b = 0
        for i in range(n**2):
            r, c = divmod(i, n)
            a_xor_b ^= grid[r][c]^(i+1)
        base = a_xor_b&-a_xor_b
        result = [0]*2
        for i in range(n**2):
            r, c = divmod(i, len(grid[0]))
            result[1 if (i+1)&base != 0 else 0] ^= i+1
            result[1 if grid[r][c]&base != 0 else 0] ^= grid[r][c]
        if any(x == result[1] for row in grid for x in row):
            result[0], result[1] = result[1], result[0]
        return result


# Time:  O(n^2)
import collections


# freq table
class Solution2(object):
    def findMissingAndRepeatedValues(self, grid):
        
        cnt = collections.Counter(x for row in grid for x in row)
        return [next(k for k, v in cnt.items() if v == 2), next(x for x in range(1, len(grid)**2+1) if x not in cnt)]
