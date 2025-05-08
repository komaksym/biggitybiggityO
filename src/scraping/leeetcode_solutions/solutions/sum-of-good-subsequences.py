# Time:  O(n)

import collections
from functools import reduce


# freq table, dp
class Solution(object):
    def sumOfGoodSubsequences(self, nums):
        
        MOD = 10**9+7
        dp = collections.defaultdict(int)
        cnt = collections.defaultdict(int)
        for x in nums:
            c = cnt[x-1]+cnt[x+1]+1
            cnt[x] = (cnt[x]+c)%MOD
            dp[x] = (dp[x]+(dp[x-1]+dp[x+1]+x*c))%MOD
        return reduce(lambda accu, x: (accu+x)%MOD, iter(dp.values()))
    
