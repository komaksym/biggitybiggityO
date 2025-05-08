# Time:  O(n + mlogm), m is the number of rides

class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        
        rides.sort()
        dp = [0]*(n+1)
        j = 0
        for i in range(1, n+1):
            dp[i] = max(dp[i], dp[i-1])
            while j < len(rides) and rides[j][0] == i:
                dp[rides[j][1]] = max(dp[rides[j][1]], dp[i]+rides[j][1]-rides[j][0]+rides[j][2])
                j += 1
        return dp[-1]
