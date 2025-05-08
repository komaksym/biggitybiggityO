# Time:  O(n)

import collections


# freq table
class Solution(object):
    def digitCount(self, num):
        
        cnt = collections.Counter(num)
        return all(cnt[str(i)] == int(x) for i, x in enumerate(num))
