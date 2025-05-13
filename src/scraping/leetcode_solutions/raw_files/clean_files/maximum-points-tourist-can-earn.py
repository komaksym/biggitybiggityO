# Time:  O(k * n^2)

# dp
class Solution(object):
    def maxScore(self, n, k, stayScore, travelScore):
        dp = [0]*n
        for i in range(k):
            dp = [max(dp[u]+stayScore[i][u], max(dp[v]+travelScore[v][u] for v in range(n))) for u in range(n)]
        return max(dp)
