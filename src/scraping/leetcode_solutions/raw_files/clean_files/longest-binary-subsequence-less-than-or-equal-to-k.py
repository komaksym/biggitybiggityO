# Time:  O(n)

# greedy
class Solution(object):
    def longestSubsequence(self, s, k):
        result, base = 0, 1
        for i in reversed(range(len(s))):
            if s[i] == '0':
                result += 1
            elif base <= k:
                k -= base
                result += 1
            if base <= k:
                base <<= 1
        return result
