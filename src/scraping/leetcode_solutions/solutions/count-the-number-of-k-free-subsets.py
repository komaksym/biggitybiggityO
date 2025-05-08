# Time:  O(n)
# Space: O(n)

import collections
import operator
from functools import reduce


# combinatorics, dp
class Solution(object):
    def countTheNumOfKFreeSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def count(x):
            y = x
            while y-k in cnt:
                y -= k
            dp = [1, 0] 
            for i in range(y, x+1, k):
                dp = [dp[0]+dp[1], dp[0]*((1<<cnt[i])-1)]
            return sum(dp)

        cnt = collections.Counter(nums)
        return reduce(operator.mul, (count(i) for i in cnt.keys() if i+k not in cnt))
