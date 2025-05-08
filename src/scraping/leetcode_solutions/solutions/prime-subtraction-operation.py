# Time:  O(p + nlogp)
# Space: O(p)

import bisect


# number theory, greedy, binary search
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
PRIMES = linear_sieve_of_eratosthenes(MAX_N-1)  
class Solution(object):
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            j = bisect.bisect_left(PRIMES, nums[i]-nums[i-1] if i-1 >= 0 else nums[i])
            if j-1 >= 0:
                nums[i] -= PRIMES[j-1]
            if i-1 >= 0 and nums[i-1] >=nums[i]:
                return False
        return True
