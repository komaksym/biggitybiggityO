# Time:  O(nlogn)

class Solution(object):
    def largestPerimeter(self, A):
        
        A.sort()
        for i in reversed(range(len(A) - 2)):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
