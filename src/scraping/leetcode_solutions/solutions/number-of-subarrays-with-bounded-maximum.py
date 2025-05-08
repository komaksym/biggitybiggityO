# Time:  O(n)

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        def count(A, bound):
            result, curr = 0, 0
            for i in A :
                curr = curr + 1 if i <= bound else 0
                result += curr
            return result

        return count(A, R) - count(A, L-1)

