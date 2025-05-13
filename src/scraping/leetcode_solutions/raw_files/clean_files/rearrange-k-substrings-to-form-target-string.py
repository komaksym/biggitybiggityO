# Time:  O(n)

import collections


# freq table
class Solution(object):
    def isPossibleToRearrange(self, s, t, k):
        cnt = collections.defaultdict(int)
        l = len(s)//k
        for i in range(0, len(s), l):
            cnt[s[i:i+l]] += 1
            cnt[t[i:i+l]] -= 1
        return all(v == 0 for v in cnt.values())
