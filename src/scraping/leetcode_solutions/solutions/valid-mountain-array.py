# Time:  O(n)

class Solution(object):
    def validMountainArray(self, A):
        i = 0
        while i+1 < len(A) and A[i] < A[i+1]:
            i += 1
        j = len(A)-1
        while j-1 >= 0 and A[j-1] > A[j]:
            j -= 1
        return 0 < i == j < len(A)-1
