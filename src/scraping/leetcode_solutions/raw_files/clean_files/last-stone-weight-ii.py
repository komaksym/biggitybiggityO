# Time:  O(2^n)

class Solution(object):
    def lastStoneWeightII(self, stones):
        dp = {0}
        for stone in stones:
            dp |= {stone+i for i in dp}
        S = sum(stones)
        return min(abs(i-(S-i)) for i in dp)
