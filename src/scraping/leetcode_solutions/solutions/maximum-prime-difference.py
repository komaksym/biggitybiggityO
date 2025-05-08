# Time:  O(r + n), r = max(nums)
# Space: O(r)

# linear sieve of eratosthenes, number theory
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


MAX_N = 100
SPF = linear_sieve_of_eratosthenes(MAX_N)
class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = next(i for i in range(len(nums)) if SPF[nums[i]] == nums[i])
        right = next(i for i in reversed(range(len(nums))) if SPF[nums[i]] == nums[i])
        return right-left
