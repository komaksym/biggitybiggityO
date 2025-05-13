# Time:  O(n)

import collections


# combinatorics
class Solution(object):
    def countAnagrams(self, s):
        MOD = 10**9+7
        fact, inv, inv_fact = [[1]*2 for _ in range(3)]
        def lazy_init(n):
            while len(inv) <= n: 
                fact.append(fact[-1]*len(inv) % MOD)
                inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD) 
                inv_fact.append(inv_fact[-1]*inv[-1] % MOD)

        def factorial(n):
            lazy_init(n)
            return fact[n]

        def inv_factorial(n):
            lazy_init(n)
            return inv_fact[n]

        def count(j, i):
            result = 1
            cnt = collections.Counter()
            for k in  range(j, i+1):
                cnt[s[k]] += 1
            result = factorial(sum(cnt.values()))
            for c in cnt.values():
                result = (result*inv_factorial(c))%MOD
            return result

        result = 1
        j = 0
        for i in range(len(s)):
            if i+1 != len(s) and s[i+1] != ' ':
                continue
            result = (result*count(j, i))%MOD
            j = i+2
        return result
