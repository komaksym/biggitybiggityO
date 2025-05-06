# Time:  O(m + n)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def nCr(n, r):  # Time: O(n), Space: O(1)
            if n-r < r:
                r = n-r
            c = 1
            for k in range(1, r+1):
                c *= n-k+1
                c //= k
            return c

        return nCr((m-1)+(n-1), n-1)


# Time:  O(m * n)
class Solution2(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            m, n  = n, m

        dp = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]
