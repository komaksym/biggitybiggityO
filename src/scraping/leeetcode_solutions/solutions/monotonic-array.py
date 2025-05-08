# Time:  O(n)

class Solution(object):
    def isMonotonic(self, A):
        
        inc, dec = False, False
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                inc = True
            elif A[i] > A[i+1]:
                dec = True
        return not inc or not dec

