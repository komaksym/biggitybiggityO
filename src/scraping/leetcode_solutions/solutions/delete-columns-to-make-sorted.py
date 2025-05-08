# Time:  O(n * l)

class Solution(object):
    def minDeletionSize(self, A):
        result = 0
        for c in range(len(A[0])):
            for r in range(1, len(A)):
                if A[r-1][c] > A[r][c]:
                    result += 1
                    break
        return result


# Time:  O(n * l)
import itertools


class Solution2(object):
    def minDeletionSize(self, A):
        result = 0
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col)-1)):
                result += 1
        return result
