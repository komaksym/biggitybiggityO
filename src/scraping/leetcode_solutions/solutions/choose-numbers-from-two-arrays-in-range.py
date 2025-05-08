# Time:  O(n^2 * v), v is max(max(nums1), max(nums2))

import collections
import itertools


# dp
class Solution(object):
    def countSubranges(self, nums1, nums2):
        MOD = 10**9+7

        result = 0
        dp = collections.Counter()
        for x, y in zip(nums1, nums2):
            new_dp = collections.Counter()
            new_dp[x] += 1
            new_dp[-y] += 1
            for v, c in dp.items():
                new_dp[v+x] = (new_dp[v+x]+c)%MOD
                new_dp[v-y] = (new_dp[v-y]+c)%MOD
            dp = new_dp
            result = (result+dp[0])%MOD
        return result
