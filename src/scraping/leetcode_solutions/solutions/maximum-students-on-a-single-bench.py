# Time:  O(n)

import collections


# hash table, unordered set
class Solution(object):
    def maxStudentsOnBench(self, students):
        
        lookup = collections.defaultdict(set)
        for s, b in students:
            lookup[b].add(s)
        return max(len(x) for x in lookup.values()) if lookup else 0
