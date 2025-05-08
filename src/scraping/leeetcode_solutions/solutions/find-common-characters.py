# Time:  O(n * l)

import collections


class Solution(object):
    def commonChars(self, A):
        
        result = collections.Counter(A[0])
        for a in A:
            result &= collections.Counter(a)
        return list(result.elements())
