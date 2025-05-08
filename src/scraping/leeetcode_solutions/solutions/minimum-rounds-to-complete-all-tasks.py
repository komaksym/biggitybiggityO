# Time:  O(n)

import collections


# math, freq table
class Solution(object):
    def minimumRounds(self, tasks):
        
        cnt = collections.Counter(tasks)
        return sum((x+2)//3 for x in cnt.values()) if 1 not in iter(cnt.values()) else -1
