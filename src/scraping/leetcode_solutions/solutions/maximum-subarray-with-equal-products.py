# Time:  precompute: O(r * log(logr)), r = MAX_NUM
#        runtime:    O(n * log(logr))

import collections


# number theory, hash table
def linear_sieve_of_eratosthenes(n): 
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

def prime_divisors(n):
    result = [[] for _ in range(n+1)]
    for p in linear_sieve_of_eratosthenes(n): 
        for i in range(p, n+1, p):
            result[i].append(p)
    return result

MAX_NUM = 10
PRIME_DIVISORS = prime_divisors(MAX_NUM)
class Solution(object):
    def maxLength(self, nums):
        
        result = 2
        lookup = collections.defaultdict(int)
        left = 0
        for right, x in enumerate(nums):
            for p in PRIME_DIVISORS[x]:
                left = max(left, lookup[p])
                lookup[p] = right+1
            result = max(result, right-left+1)
        return result
