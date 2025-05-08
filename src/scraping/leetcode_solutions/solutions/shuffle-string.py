# Time:  O(n)

# in-place solution
class Solution(object):
    def restoreString(self, s, indices):
        result = list(s)
        for i, c in enumerate(result):
            if indices[i] == i:
                continue
            move, j = c, indices[i]
            while j != i:
                result[j], move = move, result[j]
                indices[j], j = j, indices[j]
            result[i] = move
        return "".join(result)


# Time:  O(n)
import itertools


class Solution2(object):
    def restoreString(self, s, indices):
        result = ['']*len(s)
        for i, c in zip(indices, s):
            result[i] = c
        return "".join(result)
