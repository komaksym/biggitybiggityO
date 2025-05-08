# Time:  O(n)

import collections


# freq table
class Solution(object):
    def countBadPairs(self, nums):
        
        result = len(nums)*(len(nums)-1)//2
        cnt = collections.Counter()
        for i, x in enumerate(nums):
            result -= cnt[x-i]
            cnt[x-i] += 1
        return result
