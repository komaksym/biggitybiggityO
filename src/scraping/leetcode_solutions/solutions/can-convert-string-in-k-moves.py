# Time:  O(n)

import itertools


class Solution(object):
    def canConvertString(self, s, t, k):
        if len(s) != len(t):
            return False
        cnt = [0]*26
        for a, b in zip(s, t):
            diff = (ord(b)-ord(a)) % len(cnt)
            if diff != 0 and cnt[diff]*len(cnt) + diff > k:
                return False
            cnt[diff] += 1
        return True
