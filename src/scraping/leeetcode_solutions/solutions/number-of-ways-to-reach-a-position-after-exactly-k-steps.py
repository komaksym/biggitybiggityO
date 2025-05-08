# Time:  O(k)

# combinatorics
class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        
        MOD = 10**9+7
        fact, inv, inv_fact = [[1]*2 for _ in range(3)]
        def nCr(n, k):
            while len(inv) <= n: 
                fact.append(fact[-1]*len(inv) % MOD)
                inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD) 
                inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
            return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

        r = k-abs(endPos-startPos)
        return nCr(k, r//2) if r >= 0 and r%2 == 0 else 0  
