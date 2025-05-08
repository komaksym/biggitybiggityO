# Time:  O(n)

import collections


# freq table
class Solution(object):
    def mostFrequentEven(self, nums):
        cnt = collections.Counter(x for x in nums if x%2 == 0)
        return max(iter(cnt.keys()), key=lambda x: (cnt[x], -x)) if cnt else -1
