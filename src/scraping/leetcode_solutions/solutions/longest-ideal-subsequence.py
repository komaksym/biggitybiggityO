# Time:  O(n)

# dp
class Solution(object):
    def longestIdealString(self, s, k):
        dp = [0]*26
        for c in s:
            x = ord(c)-ord('a')
            dp[x] = max(dp[i] for i in range(max(x-k, 0), min(x+k+1, 26)))+1
        return max(dp)
