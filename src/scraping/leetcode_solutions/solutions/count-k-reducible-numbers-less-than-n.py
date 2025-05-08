from functools import reduce
# Time:  O(n^2)

# dp
cnt = [0]*2
class Solution(object):
    def countKReducibleNumbers(self, s, k):
        MOD = 10**9+7
        def popcount(x):
            return bin(x).count('1')

        while len(s)-1 >= len(cnt): 
            cnt.append(cnt[popcount(len(cnt))]+1)
        dp = [0]*len(s)
        curr = 0
        for i in range(len(s)):
            for j in reversed(list(range(i))):
                dp[j+1] = (dp[j+1]+dp[j])%MOD
            if s[i] != '1':
                continue
            dp[curr] = (dp[curr]+1)%MOD
            curr += 1
        return reduce(lambda accu, x: (accu+x)%MOD, (dp[i] for i in range(1, len(s)) if cnt[i] < k), 0)


# Time:  O(n^2)
# dp, combinatorics
cnt = [0]*2
class Solution2(object):
    def countKReducibleNumbers(self, s, k):
        MOD = 10**9+7
        fact, inv, inv_fact = [[1]*2 for _ in range(3)]  
        def nCr(n, k):
            while len(inv) <= n: 
                fact.append(fact[-1]*len(inv) % MOD)
                inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD) 
                inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
            return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

        def popcount(x):
            return bin(x).count('1')
      
        while len(s)-1 >= len(cnt): 
            cnt.append(cnt[popcount(len(cnt))]+1)
        result = curr = 0
        for i in range(len(s)):
            if s[i] != '1':
                continue
            for c in range((len(s)-(i+1))+1):
                if cnt[curr+c] < k:
                    result = (result+nCr(len(s)-(i+1), c))%MOD
            curr += 1
        return (result-1)%MOD

