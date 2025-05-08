# Time:  O(logn)

class Solution(object):
    def fixedPoint(self, A):
        
        left, right = 0, len(A)-1
        while left <= right:
            mid = left + (right-left)//2
            if A[mid] >= mid:
                right = mid-1
            else:
                left = mid+1
        return left if A[left] == left else -1
