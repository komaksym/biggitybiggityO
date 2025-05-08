# Time:  O(1), excluding precomputation time

# precompute
MOD = 10**9+7
MAX_N = 1000
fact = [0]*(2*MAX_N-1+1)
inv = [0]*(2*MAX_N-1+1)
inv_fact = [0]*(2*MAX_N-1+1)
fact[0] = inv_fact[0] = fact[1] = inv_fact[1] = inv[1] = 1
for i in range(2, len(fact)):
    fact[i] = fact[i-1]*i % MOD
    inv[i] = inv[MOD%i]*(MOD-MOD//i) % MOD 
    inv_fact[i] = inv_fact[i-1]*inv[i] % MOD

class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def nCr(n, k, mod):
            return (fact[n]*inv_fact[n-k] % mod) * inv_fact[k] % mod
        return nCr(n+k-1, 2*k, MOD)


# Time:  O(min(k, min(n - k)))
class Solution2(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        def nCr(n, r): 
            if n-r < r:
                return nCr(n, n-r)
            c = 1
            for k in range(1, r+1):
                c *= n-k+1
                c //= k
            return c
        return nCr(n+k-1, 2*k) % MOD
