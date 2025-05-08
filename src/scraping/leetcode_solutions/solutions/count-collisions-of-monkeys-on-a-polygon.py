# Time:  O(logn)

# combinatorics, fast exponentiation
class Solution(object):
    def monkeyMove(self, n):
        MOD = 10**9+7
        return (pow(2, n, MOD)-2)%MOD
