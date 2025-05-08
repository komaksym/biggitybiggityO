# Time:  O(m * n)

class Solution(object):
    def maxPoints(self, points):
        
        dp = points[0]
        for i in range(1, len(points)):
            prefix = [0]*len(points[i])
            prefix[0] = dp[0]
            for j in range(1, len(points[i])):
                prefix[j] = max(prefix[j-1], dp[j]+j)
            suffix = [0]*len(points[i])
            suffix[-1] = dp[-1]-(len(points[i])-1)
            for j in reversed(range(len(points[i])-1)):
                suffix[j] = max(suffix[j+1], dp[j]-j)
            new_dp = [0]*len(points[i])
            for j in range(len(points[i])):
                new_dp[j] = max(prefix[j]-j, suffix[j]+j)+points[i][j]
            dp = new_dp
        return max(dp)
