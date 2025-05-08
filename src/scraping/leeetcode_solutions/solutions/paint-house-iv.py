# Time:  O(n * l^4)
# Space: O(l^2)

# dp
class Solution(object):
    def minCost(self, n, cost):
        """
        :type n: int
        :type cost: List[List[int]]
        :rtype: int
        """
        l = len(cost[0])
        dp = [[0]*l for i in range(l)]
        for k in range(n//2):
            new_dp = [[float("inf")]*l for i in range(l)]
            for i in range(l):
                for j in range(l):
                    if j == i:
                        continue
                    for ni in range(l):
                        if ni == i:
                            continue
                        for nj in range(l):
                            if nj == j or ni == nj:
                                continue
                            new_dp[ni][nj] = min(new_dp[ni][nj], dp[i][j]+cost[k][ni]+cost[~k][nj])
            dp = new_dp
        return min(dp[i][j] for i in range(l) for j in range(l) if i != j)
