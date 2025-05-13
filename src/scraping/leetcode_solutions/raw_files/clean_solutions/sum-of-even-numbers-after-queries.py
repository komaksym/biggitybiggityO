# Time:  O(n + q)

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        total = sum(v for v in A if v % 2 == 0)
        
        result = []
        for v, i in queries:
            if A[i] % 2 == 0:
                total -= A[i]
            A[i] += v
            if A[i] % 2 == 0:
                total += A[i]
            result.append(total)
        return result
