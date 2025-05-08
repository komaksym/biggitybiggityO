# Time:  O(n)

import collections


class Solution(object):
    def distinctSubseqII(self, S):
        
        MOD = 10**9+7
        result, dp = 0, [0]*26
        for c in S:
            result, dp[ord(c)-ord('a')] = (result+((result+1)-dp[ord(c)-ord('a')]))%MOD, (result+1)%MOD
        return result
