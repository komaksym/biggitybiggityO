# Time:  O(logn)

class Solution(object):
    def bitwiseComplement(self, N):
        mask = 1
        while N > mask:
            mask = mask*2+1
        return mask-N
