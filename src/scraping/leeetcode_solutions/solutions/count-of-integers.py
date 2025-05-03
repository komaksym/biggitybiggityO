from functools import reduce
# Time:  O(n * m), m = max_sum
# Space: O(n + m)

# combinatorics, dp
class Solution(object):
    def count(self, num1, num2, min_sum, max_sum):
        """
        :type num1: str
        :type num2: str
        :type min_sum: int
        :type max_sum: int
        :rtype: int
        """
        MOD = 10**9+7
        def f(x):
            dp = [[0]*(max_sum+1) for _ in range(2)]
            dp[0][0] = dp[1][0] = 1
            for i in reversed(range(len(x))):
                new_dp = [[0]*(max_sum+1) for _ in range(2)]
                for t in range(2):
                    for total in range(max_sum+1):
                        for d in range(min((int(x[i]) if t else 9), total)+1):
                            new_dp[t][total] = (new_dp[t][total]+dp[int(t and d == int(x[i]))][total-d])%MOD
                dp = new_dp
            return reduce(lambda x, y: (x+y)%MOD, (dp[1][total] for total in range(min_sum, max_sum+1)))

        return (f(num2)-f(str(int(num1)-1)))%MOD
