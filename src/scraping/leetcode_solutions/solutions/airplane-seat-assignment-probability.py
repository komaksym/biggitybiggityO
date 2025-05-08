# Time:  O(1)
# Space: O(1)

class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        return 0.5 if n != 1 else 1.0

# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        dp = [0.0]*2
        dp[0] = 1.0 
        for i in range(2, n+1):
            dp[(i-1)%2] = 1.0/i+dp[(i-2)%2]*(i-2)/i
        return dp[(n-1)%2]
