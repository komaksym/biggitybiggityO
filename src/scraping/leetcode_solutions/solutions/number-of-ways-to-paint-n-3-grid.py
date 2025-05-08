# Time:  O(logn)

import itertools


class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        def matrix_expo(A, K):
            result = [[int(i==j) for j in range(len(A))]
                       for i in range(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        def matrix_mult(A, B):
            ZB = list(zip(*B))
            return [[sum(a*b % MOD for a, b in zip(row, col)) % MOD
                     for col in ZB] for row in A]
        
        MOD = 10**9 + 7
        T = [[3, 2],
             [2, 2]]
        return sum(matrix_mult([[6, 6]], matrix_expo(T, n-1))[0]) % MOD 


# Time:  O(n)
class Solution2(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        aba, abc = 6, 6
        for _ in range(n-1):
            aba, abc = (3*aba%MOD + 2*abc%MOD)%MOD, \
                       (2*abc%MOD + 2*aba%MOD)%MOD
        return (aba+abc)%MOD
