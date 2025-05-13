from functools import reduce
# Time:  O(n * k)

# knapsack dp, combinatorics, sliding window, two pointers
class Solution(object):
    def kInversePairs(self, n, k):
        MOD = 10**9+7
        dp = [1]
        for i in range(n):
            new_dp = [0]*min(len(dp)+((i+1)-1), k+1)
            for j in range(len(new_dp)):
                new_dp[j] = dp[j] if j < len(dp) else 0
                if j-1 >= 0:
                    new_dp[j] = (new_dp[j]+new_dp[j-1])%MOD
                if j-(i+1) >= 0:
                    new_dp[j] = (new_dp[j]-dp[j-(i+1)])%MOD
            dp = new_dp
        return dp[k] if k < len(dp) else 0


# Time:  O(n * k)
# knapsack dp, combinatorics, sliding window, two pointers
class Solution2(object):
    def kInversePairs(self, n, k):
        MOD = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1
        for i in range(n):
            new_dp = [0]*len(dp)
            for j in range(len(dp)):
                new_dp[j] = dp[j]
                if j-1 >= 0:
                    new_dp[j] = (new_dp[j]+new_dp[j-1])%MOD
                if j-(i+1) >= 0:
                    new_dp[j] = (new_dp[j]-dp[j-(i+1)])%MOD
            dp = new_dp
        return dp[-1]


# Time:  O(n * k)
# knapsack dp, combinatorics, sliding window, two pointers
class Solution3(object):
    def kInversePairs(self, n, k):
        MOD = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1
        for i in range(n):
            new_dp = [0]*len(dp)
            curr = 0
            for j in range(len(dp)):
                curr = (curr+dp[j])%MOD
                if j-(i+1) >= 0:
                    curr = (curr-dp[j-(i+1)])%MOD
                new_dp[j] = curr
            dp = new_dp
        return dp[-1]


# Time:  O(n^2 * k)
# knapsack dp, combinatorics
class Solution_TLE(object):
    def kInversePairs(self, n, k):
        MOD = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1
        for i in range(n):
            dp = [reduce(lambda total, k: (total+dp[j-k])%MOD, range(min(i+1, j+1)), 0) for j in range(len(dp))]
        return dp[-1]%MOD


class Solution_ConstructPermutation(object):
    def kInversePairs(self, n, k):
        MOD = 10**9+7
        dp = [[] for _ in range(k+1)]
        dp[0].append([])
        for i in range(n):
            dp = [[[x+int(x >= i-k) for x in p]+[i-k] for k in range(min(i+1, j+1)) for p in dp[j-k]] for j in range(len(dp))]
        assert(all(sum(int(p[j] > p[i]) for i in range(n) for j in range(i)) == len(dp)-1) for p in dp[-1])
        return len(dp[-1])%MOD


class Solution_ConstructPermutation2(object):
    def kInversePairs(self, n, k):
        MOD = 10**9+7
        dp = [[] for _ in range(k+1)]
        dp[0].append([])
        for i in range(n):
            dp = [[p[:len(p)-k]+[i]+p[len(p)-k:] for k in range(min(i+1, j+1)) for p in dp[j-k]] for j in range(len(dp))]
        assert(all(sum(int(p[j] > p[i]) for i in range(n) for j in range(i)) == len(dp)-1) for p in dp[-1])
        return len(dp[-1])%MOD
