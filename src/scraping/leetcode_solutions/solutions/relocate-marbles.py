# Time:  O(nlogn)

import itertools


# hash table, sort
class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        
        lookup = set(nums)
        for a, b in zip(moveFrom, moveTo):
            lookup.remove(a)
            lookup.add(b)
        return sorted(lookup)
