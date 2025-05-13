# Time:  O(n + r), r = max(nums)
from functools import reduce

# combinatorics, stars and bars
class Solution(object):
    def countOfPairs(self, nums):
        fact, inv, inv_fact = [[1]*2 for _ in range(3)]
        def nCr(n, k):
            while len(inv) <= n: 
                fact.append(fact[-1]*len(inv) % MOD)
                inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD) 
                inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
            return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD
    
        def nHr(n, r):
            return nCr(n+r-1, r)

        MOD = 10**9+7
        cnt = nums[-1]-sum(max(nums[i]-nums[i-1], 0) for i in range(1, len(nums)))
        return nHr(len(nums)+1, cnt) if cnt >= 0 else 0
# dp, prefix sum
class Solution2(object):
    def countOfPairs(self, nums):
        MOD = 10**9+7
        dp = [int(i <= nums[0]) for i in range(max(nums)+1)] 
        for i in range(1, len(nums)):
            new_dp = [0]*len(dp)
            diff = max(nums[i]-nums[i-1], 0)
            for j in range(diff, nums[i]+1):
                new_dp[j] = (new_dp[j-1]+dp[j-diff])%MOD
            dp = new_dp
        return reduce(lambda accu, x: (accu+x)%MOD, dp, 0)
