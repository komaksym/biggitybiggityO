# Time:  O(n^2)

# dp
class Solution(object):
    def houseOfCards(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1) 
        dp[0] = 1
        for t in range(1, (n+1)//3+1):
            for i in reversed(range(3*t-1, n+1)):
                dp[i] += dp[i-(3*t-1)]
        return dp[n]


# Time:  O(n^3)
# dp
class Solution_TLE(object):
    def houseOfCards(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range((n+1)//3+1)] 
        dp[0][0] = 1
        for t in range(1, (n+1)//3+1):
            for i in range(3*t-1, n+1):
                dp[t][i] = sum(dp[j][i-(3*t-1)] for j in range(t))
        return sum(dp[t][n] for t in range((n+1)//3+1))
