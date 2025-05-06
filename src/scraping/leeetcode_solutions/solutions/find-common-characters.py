# Time:  O(n * l)

import collections


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = collections.Counter(A[0])
        for a in A:
            result &= collections.Counter(a)
        return list(result.elements())
