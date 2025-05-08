# Time:  precompute: O(sqrt(MAX_N))
#        runtime:    O(m + nlog(logn)), m = len(nums), n = max(nums)

# number theory
def linear_sieve_of_eratosthenes(n):
    primes = []
    spf = [-1]*(n+1) 
    for i in range(2, n+1):
        if spf[i] == -1:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if i*p > n or p > spf[i]:
                break
            spf[i*p] = p
    return primes 


MAX_N = 10**3
PRIMES = linear_sieve_of_eratosthenes(int(MAX_N**0.5))  
class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = set()
        for x in set(nums): 
            for p in PRIMES:
                if p > x:
                    break
                if x%p:
                    continue
                result.add(p)
                while x%p == 0:
                    x //= p
            if x != 1: 
                result.add(x)
        return len(result)
