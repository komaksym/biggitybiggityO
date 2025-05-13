# Time:  O(logn)

import itertools


class Solution(object):
    def fib(self, N):
        def matrix_expo(A, K):
            result = [[int(i==j) for j in range(len(A))] \
                      for i in range(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        def matrix_mult(A, B):
            ZB = list(zip(*B))
            return [[sum(a*b for a, b in zip(row, col)) \
                     for col in ZB] for row in A]

        T = [[1, 1],
             [1, 0]]
        return matrix_mult([[1, 0]], matrix_expo(T, N))[0][1] 


# Time:  O(n)
class Solution2(object):
    def fib(self, N):
        prev, current = 0, 1
        for i in range(N):
            prev, current = current, prev + current,
        return prev
