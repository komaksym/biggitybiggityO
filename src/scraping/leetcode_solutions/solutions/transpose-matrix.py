# Time:  O(r * c)


class Solution(object):
    def transpose(self, A):
        result = [[None] * len(A) for _ in range(len(A[0]))]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                result[c][r] = val
        return result


# Time:  O(r * c)
class Solution2(object):
    def transpose(self, A):
        return list(zip(*A))

