# Time:  precompute:  O(sqrt(r))
#        runtime:     O(logr + log(sqrt(r))) = O(logr)
# Space: O(sqrt(r))

import bisect


# number theory, binary search
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


MAX_R = 10**9
PRIMES = linear_sieve_of_eratosthenes(int(MAX_R**0.5))
class Solution(object):
    def nonSpecialCount(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        def count(x):
            return x-bisect.bisect_right(PRIMES, int(x**0.5))

        return count(r)-count(l-1)
