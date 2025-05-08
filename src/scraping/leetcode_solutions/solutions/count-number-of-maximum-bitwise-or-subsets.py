# Time:  O(min(2^n, m * n)), m is the 'bitwise or' of nums
# Space: O(min(2^n, m))

import collections
from functools import reduce


class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = collections.Counter([0])
        for x in nums:
            for k, v in list(dp.items()):
                dp[k|x] += v
        return dp[reduce(lambda x, y: x|y, nums)]
