from functools import reduce
# Time:  O(n + m + logr), r is max(numsDivide)

# gcd
class Solution(object):
    def minOperations(self, nums, numsDivide):
        def gcd(a, b): 
            while b:
                a, b = b, a%b
            return a

        g = reduce(gcd, numsDivide)
        mn = float("inf")
        for x in nums:
            if g%x == 0:
                mn = min(mn, x)
        return sum(x < mn for x in nums) if mn != float("inf") else -1
