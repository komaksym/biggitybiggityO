# Time:  O(n)

class Solution(object):
    def maxRotateFunction(self, A):
        s = sum(A)
        fi = 0
        for i in range(len(A)):
            fi += i * A[i]

        result = fi
        for i in range(1, len(A)+1):
            fi += s - len(A) * A[-i]
            result = max(result, fi)
        return result

