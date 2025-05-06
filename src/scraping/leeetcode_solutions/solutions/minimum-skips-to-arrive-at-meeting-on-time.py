# Time:  O(n^2)

class Solution(object):
    def minSkips(self, dist, speed, hoursBefore):
        """
        :type dist: List[int]
        :type speed: int
        :type hoursBefore: int
        :rtype: int
        """
        def ceil(a, b):
            return (a+b-1)//b

        dp = [0]*((len(dist)-1)+1)  # dp[i]: (min time by i skips) * speed
        for i, d in enumerate(dist):
            for j in reversed(range(len(dp))):
                dp[j] = ceil(dp[j]+d, speed)*speed if i < len(dist)-1 else dp[j]+d
                if j-1 >= 0:
                    dp[j] = min(dp[j], dp[j-1]+d)
        target = hoursBefore*speed
        for i in range(len(dist)):
            if dp[i] <= target:
                return i
        return -1
