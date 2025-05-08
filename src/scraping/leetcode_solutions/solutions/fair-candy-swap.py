# Time:  O(m + n)

class Solution(object):
    def fairCandySwap(self, A, B):
        diff = (sum(A)-sum(B))//2
        setA = set(A)
        for b in set(B):
            if diff+b in setA:
                return [diff+b, b]
        return []

