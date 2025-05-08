# Time:  O(n * k) = O(3 * n)
# Space: O(n + k) = O(n)

import collections


# freq table, dp
class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        K = 3
        cnt = collections.Counter()
        dp = [0]*K 
        for x in nums:
            cnt[x] += 1
            other_cnt = 1
            for i in range(K):
                dp[i] += other_cnt
                other_cnt = dp[i]-cnt[x]*other_cnt
        return dp[K-1]
