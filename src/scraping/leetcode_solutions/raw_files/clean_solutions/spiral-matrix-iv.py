# Time:  O(m * n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        pass


# linked list, array
class Solution(object):
    def spiralMatrix(self, m, n, head):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[-1]*n for _ in range(m)]
        i = j = d = 0
        while head:
            result[i][j] = head.val
            if not (0 <= i+directions[d][0] < m and 0 <= j+directions[d][1] < n and result[i+directions[d][0]][j+directions[d][1]] == -1):
                d = (d+1)%4
            i, j = i+directions[d][0], j+directions[d][1]
            head = head.__next__
        return result
