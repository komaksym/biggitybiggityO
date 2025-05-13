# Time:  O(m + n)

import collections


class Solution(object):
    def countWords(self, words1, words2):
        cnt = collections.Counter(words1)
        for c in words2:
            if cnt[c] < 2:
                cnt[c] -= 1
        return sum(v == 0 for v in cnt.values())
