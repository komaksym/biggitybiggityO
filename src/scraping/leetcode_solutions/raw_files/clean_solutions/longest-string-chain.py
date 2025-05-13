# Time:  O(n * l^2)

import collections


class Solution(object):
    def longestStrChain(self, words):
        words.sort(key=len)
        dp = collections.defaultdict(int)
        for w in words:
            for i in range(len(w)):
                dp[w] = max(dp[w], dp[w[:i]+w[i+1:]]+1)
        return max(dp.values())
