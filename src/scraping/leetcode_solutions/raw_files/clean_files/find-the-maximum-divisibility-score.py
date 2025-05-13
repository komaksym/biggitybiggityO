# Time:  O(n * d)

# brute force
class Solution(object):
    def maxDivScore(self, nums, divisors):
        return max(divisors, key=lambda d: (sum(x%d == 0 for x in nums), -d))
