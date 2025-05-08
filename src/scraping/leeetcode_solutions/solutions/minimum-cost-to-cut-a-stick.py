# Time:  O(n^3)

class Solution(object):
    def minCost(self, n, cuts):
        
        sorted_cuts = sorted(cuts + [0, n])
        dp = [[0]*len(sorted_cuts) for _ in range(len(sorted_cuts))]
        for l in range(2, len(sorted_cuts)):
            for i in range(len(sorted_cuts)-l):
                dp[i][i+l] = min(dp[i][j]+dp[j][i+l] for j in range(i+1, i+l)) + \
                             sorted_cuts[i+l]-sorted_cuts[i]
        return dp[0][len(sorted_cuts)-1]
