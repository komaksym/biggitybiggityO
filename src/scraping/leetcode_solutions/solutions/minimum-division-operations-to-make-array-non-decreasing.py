# Time:  precompute: O(r)
#        runtime:    O(n)

# greedy, number theory
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

MAX_N = 10**6
SPF = linear_sieve_of_eratosthenes(MAX_N)
class Solution(object):
    def minOperations(self, nums):
        result = 0
        for i in reversed(range(len(nums)-1)):
            if nums[i] <= nums[i+1]:
                continue
            if SPF[nums[i]] > nums[i+1]:
                return -1
            nums[i] = SPF[nums[i]]
            result += 1
        return result
