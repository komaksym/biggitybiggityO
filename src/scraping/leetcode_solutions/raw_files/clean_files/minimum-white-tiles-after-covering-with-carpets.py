# Time:  O(m * n)

# dp
class Solution(object):
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        dp = [[0]*(numCarpets+1) for _ in range(len(floor)+1)] 
        for i in range(1, len(dp)):
            dp[i][0] = dp[i-1][0] + int(floor[i-1])
            for j in range(1, numCarpets+1):
                dp[i][j] = min(dp[i-1][j] + int(floor[i-1]), dp[max(i-carpetLen, 0)][j-1])
        return dp[-1][-1]
