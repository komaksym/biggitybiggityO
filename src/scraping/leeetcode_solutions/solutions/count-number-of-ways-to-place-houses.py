# Time:  O(logn)

import itertools


# matrix exponentiation
class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        def matrix_mult(A, B):
            ZB = list(zip(*B))
            return [[sum(a*b % MOD for a, b in zip(row, col)) % MOD for col in ZB] for row in A]
 
        def matrix_expo(A, K):
            result = [[int(i == j) for j in range(len(A))] for i in range(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        T = [[1, 1],
             [1, 0]]
        return pow(matrix_mult([[2, 1]], matrix_expo(T, n-1))[0][0], 2, MOD)  # [a1, a0] * T^(n-1) = [an, a(n-1)]

    
# Time:  O(n)
# dp
class Solution2(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        prev, curr = 1, 2
        for _ in range(n-1):
            prev, curr = curr, (prev+curr)%MOD
        return pow(curr, 2, MOD)
