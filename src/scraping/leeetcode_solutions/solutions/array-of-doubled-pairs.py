# Time:  O(n + klogk)

import collections


class Solution(object):
    def canReorderDoubled(self, A):
        
        count = collections.Counter(A)
        for x in sorted(count, key=abs):
            if count[x] > count[2*x]:
                return False
            count[2*x] -= count[x]
        return True
