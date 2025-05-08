# Time:  O(1)
# Space: O(1)


class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 7:
            return N
        if N == 10:
            return 20 

        n = N // 5 + 1 
        n3 = 5*n - N - 1
        n4 = n - n3
        return 3**n3 * 4**n4


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 7:
            return N
        dp = list(range(N+1))
        for i in range(7, N+1):
            dp[i % 6] = max(dp[(i-4) % 6]*3, dp[(i-5) % 6]*4)
        return dp[N % 6]

