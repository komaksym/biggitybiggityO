# Time:  O(n)

class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        MOD = 10**9+7

        dp = [0]*len(nextVisit)
        for i in range(1, len(dp)):
            dp[i] = (dp[i-1]+1+(dp[i-1]-dp[nextVisit[i-1]])+1)%MOD
        return dp[-1]
