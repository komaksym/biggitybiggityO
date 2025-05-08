# Time:  O(n^2)

import itertools


class Solution(object):
    def minSwaps(self, grid):
        
        result = 0
        for target in reversed(range(1, len(grid))):
            row_idx = len(grid)-1-target
            while row_idx < len(grid):
                row = grid[row_idx]
                if not sum(itertools.islice(row, len(row)-target, len(row))):
                    break
                row_idx += 1
            else:
                return -1
            while row_idx != len(grid)-1-target:
                grid[row_idx], grid[row_idx-1] = grid[row_idx-1], grid[row_idx]
                result += 1
                row_idx -= 1
        return result
