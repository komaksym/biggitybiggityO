# Time:  O(n + logm)

# combinatorics, fast exponentiation
MOD = 10**9+7
FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
def nCr(n, k):
    while len(INV) <= n: 
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD) 
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)
    return (FACT[n]*INV_FACT[n-k] % MOD) * INV_FACT[k] % MOD


class Solution(object):
    def countGoodArrays(self, n, m, k):
        return (nCr(n-1, k)*(m*pow(m-1, (n-1)-k, MOD)))%MOD
