# Time:  O(n^2 * k)

# dp
class Solution(object):
    def longestPalindromicSubsequence(self, s, k):
        
        dp = [[[1 if i == j else 0 for _ in range(k+1)] for j in range(len(s))] for i in range(len(s))]
        for i in reversed(range(len(s)-1)):
            for j in range(i+1, len(s)):
                for x in range(k+1):
                    if s[i] == s[j]:
                        dp[i][j][x] = dp[i+1][j-1][x]+2
                    else:
                        dp[i][j][x] = max(dp[i+1][j][x], dp[i][j-1][x])
                        diff = abs(ord(s[i])-ord(s[j]))
                        c = min(diff, 26-diff)
                        if x >= c:
                            dp[i][j][x] = max(dp[i][j][x], dp[i+1][j-1][x-c]+2)
        return dp[0][-1][k]
