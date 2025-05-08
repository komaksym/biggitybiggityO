# Time:  O(m * n)

import heapq


class Solution(object):
    def minFallingPathSum(self, arr):
        
        for i in range(1, len(arr)):
            smallest_two = heapq.nsmallest(2, arr[i-1])
            for j in range(len(arr[0])):
                arr[i][j] += smallest_two[1] if arr[i-1][j] == smallest_two[0] else smallest_two[0]
        return min(arr[-1])
