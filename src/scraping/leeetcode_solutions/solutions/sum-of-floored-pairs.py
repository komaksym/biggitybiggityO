# Time:  O(n/1+n/2+...+n/n) = O(nlogn), n is the max of nums

import collections
from functools import reduce


class Solution(object):
    def sumOfFlooredPairs(self, nums):
        
        MOD = 10**9+7
        prefix, counter = [0]*(max(nums)+1), collections.Counter(nums)
        for num, cnt in counter.items():
            for j in range(num, len(prefix), num):
                prefix[j] += counter[num]
        for i in range(len(prefix)-1):
            prefix[i+1] += prefix[i]
        return reduce(lambda total, num: (total+prefix[num])%MOD, nums, 0)
