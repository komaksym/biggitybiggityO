# Time:  O(logn)

# variant of "343. integer break"
class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        MOD = 10**9 + 7
        if primeFactors <= 3:
            return primeFactors
        if primeFactors % 3 == 0:  # 6 => 3*3
            return pow(3, primeFactors//3, MOD)
        if primeFactors % 3 == 1:  # 4 => 2*2 
            return (2*2*pow(3, (primeFactors-4)//3, MOD)) % MOD
        return (2*pow(3, (primeFactors-2)//3, MOD)) % MOD  # 5 => 2*3
