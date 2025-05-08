# Time:  O(n)

# greedy
class Solution(object):
    def maximumXorProduct(self, a, b, n):
        
        MOD = 10**9+7
        for i in reversed(range(n)):
            base = 1<<i
            if min(a, b)&base == 0:
                a, b = a^base, b^base
        return (a%MOD)*(b%MOD)%MOD
