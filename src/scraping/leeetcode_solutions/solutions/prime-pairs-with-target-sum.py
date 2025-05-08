# Time:  O(n)

# number theory
class Solution(object):
    def findPrimePairs(self, n):
        
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
            return spf 

        spf = linear_sieve_of_eratosthenes(n)
        return [[i, n-i] for i in range(2, n//2+1) if spf[i] == i and spf[n-i] == n-i]
