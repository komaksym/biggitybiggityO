from functools import reduce
# Time:  O(m * n), m is the max of rollMax

class Solution(object):
    def dieSimulator(self, n, rollMax):
        
        MOD = 10**9+7
        def sum_mod(array):
            return reduce(lambda x, y: (x+y)%MOD, array)

        dp = [[1] + [0]*(rollMax[i]-1) for i in range(6)] 
        for _ in range(n-1):
            new_dp = [[0]*rollMax[i] for i in range(6)]
            for i in range(6):
                for k in range(rollMax[i]):
                    for j in range(6):
                        if i == j:
                            if k < rollMax[i]-1: 
                                new_dp[j][k+1] = (new_dp[j][k+1]+dp[i][k])%MOD
                        else:
                            new_dp[j][0] = (new_dp[j][0]+dp[i][k])%MOD
            dp = new_dp
        return sum_mod(sum_mod(row) for row in dp)
