# Time:  O(n)

class Solution(object):
    def longestOnes(self, A, K):
        
        result, i = 0, 0
        for j in range(len(A)):
            K -= int(A[j] == 0)
            while K < 0:
                K += int(A[i] == 0)
                i += 1
            result = max(result, j-i+1)
        return result
