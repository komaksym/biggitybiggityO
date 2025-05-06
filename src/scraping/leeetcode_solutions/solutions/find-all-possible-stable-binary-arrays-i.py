# Time:  O(n * m)

# dp
class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]
        for i in range(zero+1):
            dp[i][0][0] = 1 if i <= limit else 0
        for j in range(one+1):
            dp[0][j][1] = 1 if j <= limit else 0
        for i in range(1, zero+1):
            for j in range(1, one+1):
                dp[i][j][0] = (dp[i-1][j][0]+dp[i-1][j][1])%MOD
                dp[i][j][1] = (dp[i][j-1][0]+dp[i][j-1][1])%MOD
                if i-limit-1 >= 0:
                    dp[i][j][0] = (dp[i][j][0]-dp[i-limit-1][j][1])%MOD
                if j-limit-1 >= 0:
                    dp[i][j][1] = (dp[i][j][1]-dp[i][j-limit-1][0])%MOD
        return (dp[-1][-1][0]+dp[-1][-1][1])%MOD


# Time:  O(n * m * l)
# dp
class Solution2(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]
        dp[0][0][0] = dp[0][0][1] = 1
        for i in range(zero+1):
            for j in range(one+1):
                for k in range(1, limit+1):
                    if i-k >= 0:
                        dp[i][j][0] = (dp[i][j][0]+dp[i-k][j][1])%MOD
                    if j-k >= 0:
                        dp[i][j][1] = (dp[i][j][1]+dp[i][j-k][0])%MOD
        return (dp[-1][-1][0]+dp[-1][-1][1])%MOD
