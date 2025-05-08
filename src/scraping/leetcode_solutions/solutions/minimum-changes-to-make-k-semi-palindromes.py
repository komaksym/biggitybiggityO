# Time:  O(n * nlogn + n^3 + n^2 * k) = O(n^3)

# number theory, dp
class Solution(object):
    def minimumChanges(self, s, k):
        divisors = [[] for _ in range(len(s)+1)]
        for i in range(1, len(divisors)): 
            for j in range(i, len(divisors), i):
                divisors[j].append(i)
        dp = [[{} for _ in range(len(s))] for _ in range(len(s))]
        for l in range(1, len(s)+1): 
            for left in range(len(s)-l+1):
                right = left+l-1
                for d in divisors[l]:
                    dp[left][right][d] = (dp[left+d][right-d][d] if left+d < right-d else 0)+sum(s[left+i] != s[(right-(d-1))+i] for i in range(d))
        dp2 = [[min(dp[i][j][d] for d in divisors[j-i+1] if d != j-i+1) if i < j else 0 for j in range(len(s))] for i in range(len(s))] 
        dp3 = [len(s)]*(len(s)+1)
        dp3[0] = 0
        for l in range(k): 
            new_dp3 = [len(s)]*(len(s)+1)
            for i in range(len(s)):
                for j in range(l*2, i): 
                    new_dp3[i+1]= min(new_dp3[i+1], dp3[j]+dp2[j][i])
            dp3 = new_dp3
        return dp3[len(s)]


# Time:  O(n * nlogn + n^3 + n^2 * k) = O(n^3)
# number theory, dp
class Solution2(object):
    def minimumChanges(self, s, k):
        divisors = [[] for _ in range(len(s)+1)]
        for i in range(1, len(divisors)): 
            for j in range(i, len(divisors), i):
                divisors[j].append(i)
        dp = [[{} for _ in range(len(s))] for _ in range(len(s))]
        for l in range(1, len(s)+1): 
            for left in range(len(s)-l+1):
                right = left+l-1
                for d in divisors[l]:
                    dp[left][right][d] = (dp[left+d][right-d][d] if left+d < right-d else 0)+sum(s[left+i] != s[(right-(d-1))+i] for i in range(d))
        dp2 = [[len(s)]*(k+1) for _ in range(len(s)+1)]
        dp2[0][0] = 0
        for i in range(len(s)): 
            for j in range(i):
                c = min(dp[j][i][d] for d in divisors[i-j+1] if d != i-j+1)
                for l in range(k):
                    dp2[i+1][l+1] = min(dp2[i+1][l+1], dp2[j][l]+c)
        return dp2[len(s)][k]


# Time:  O(n^2 * nlogn + n^2 * k) = O(n^3 * logn)
# number theory, dp
class Solution3(object):
    def minimumChanges(self, s, k):
        def min_dist(left, right): 
            return min(sum(s[left+i] != s[right-((i//d+1)*d-1)+(i%d)] for i in range((right-left+1)//2))
 for d in divisors[right-left+1])

        divisors = [[] for _ in range(len(s)+1)]
        for i in range(1, len(divisors)): 
            for j in range(i+i, len(divisors), i):
                divisors[j].append(i)
        dp = [[len(s)]*(k+1) for _ in range(len(s)+1)]
        dp[0][0] = 0
        for i in range(len(s)): 
            for j in range(i):
                c = min_dist(j, i)
                for l in range(k):
                    dp[i+1][l+1] = min(dp[i+1][l+1], dp[j][l]+c)
        return dp[len(s)][k]
