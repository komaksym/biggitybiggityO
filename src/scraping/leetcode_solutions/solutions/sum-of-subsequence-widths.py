# Time:  O(n)
# Spce:  O(1)

class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        M = 10**9+7
        result, c = 0, 1
        A.sort()
        for i in range(len(A)):
            result = (result + (A[i]-A[len(A)-1-i])*c % M) % M
            c = (c<<1) % M
        return result

