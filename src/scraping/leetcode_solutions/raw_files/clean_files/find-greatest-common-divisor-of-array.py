# Time:  O(n)

import fractions


class Solution(object):
    def findGCD(self, nums):
        return fractions.gcd(min(nums), max(nums))
