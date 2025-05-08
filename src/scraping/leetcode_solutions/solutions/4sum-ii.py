# Time:  O(n^2)

import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        
        A_B_sum = collections.Counter(a+b for a in A for b in B)
        return sum(A_B_sum[-c-d] for c in C for d in D)

