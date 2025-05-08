# Time:  O(n^2)

import itertools


# dp, backtracing
class Solution(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        
        def check(s1, s2):
            return len(s1) == len(s2) and sum(a != b for a, b in zip(s1, s2)) == 1

        dp = [[1, -1] for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(i+1, n):
                if groups[i] != groups[j] and check(words[j], words[i]):
                    dp[i] = max(dp[i], [dp[j][0]+1, j])
        result = []
        i = max(range(n), key=lambda x: dp[x])
        while i != -1:
            result.append(words[i])
            i = dp[i][1]
        return result


# Time:  O(n^2)
import itertools


# dp, backtracing
class Solution2(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        
        def check(s1, s2):
            return len(s1) == len(s2) and sum(a != b for a, b in zip(s1, s2)) == 1

        dp = [[1, -1] for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and check(words[j], words[i]):
                    dp[i] = max(dp[i], [dp[j][0]+1, j])
        result = []
        i = max(range(n), key=lambda x: dp[x])
        while i != -1:
            result.append(words[i])
            i = dp[i][1]
        result.reverse()
        return result


# Time:  O(n^2)
import itertools


# lis dp
class Solution3(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        
        def check(s1, s2):
            return len(s1) == len(s2) and sum(a != b for a, b in zip(s1, s2)) == 1

        dp = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and check(words[j], words[i]) and len(dp[j]) > len(dp[i]):
                    dp[i] = dp[j]
            dp[i] = dp[i]+[i]
        return [words[x] for x in max(dp, key=lambda x: len(x))]
