# Time:  O(k * n) = O(n)

# dp
class Solution(object):
    def numberOfWays(self, s):
        K = 3
        dp = [[0]*2 for _ in range(K)] 
        for c in s:
            j = ord(c)-ord('0')
            dp[0][j] += 1
            for i in range(1, len(dp)):
                dp[i][j] += dp[i-1][1^j]
        return dp[-1][0]+dp[-1][1]
