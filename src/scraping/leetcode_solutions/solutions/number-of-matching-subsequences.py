# Time:  O(n + w), n is the size of S, w is the size of words

import collections


class Solution(object):
    def numMatchingSubseq(self, S, words):
        waiting = collections.defaultdict(list)
        for word in words:
            it = iter(word)
            waiting[next(it, None)].append(it)
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])

