# Time:  O(n)

import collections


# hash table
class Solution(object):
    def minimumSeconds(self, nums):
        lookup = collections.defaultdict(int)
        dist = collections.defaultdict(int)
        for i in range(2*len(nums)):
            x = nums[i%len(nums)]
            dist[x] = max(dist[x], i-lookup[x])
            lookup[x] = i
        return min(dist.values())//2
