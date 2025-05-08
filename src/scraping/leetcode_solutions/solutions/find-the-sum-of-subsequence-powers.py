# Time:  O(n^2 + len(diffs) * n * k) = O(n^3 * k) at most

# sort, dp, prefix sum, two pointers
class Solution(object):
    def sumOfPowers(self, nums, k):
        MOD = 10**9+7
        nums.sort()
        result = prev = 0
        for mn in sorted({nums[j]-nums[i] for i in range(len(nums)) for j in range(i+1, len(nums))}, reverse=True):
            dp = [[0]*(k+1) for _ in range(len(nums)+1)]
            dp[0][0] = 1
            j = 0
            for i in range(len(nums)):
                j = next((j for j in range(j, len(nums)) if nums[i]-nums[j] < mn), len(nums))
                for l in range(1, k+1):
                    dp[i+1][l] = (dp[i+1][l]+dp[(j-1)+1][l-1])%MOD 
                for l in range(k+1):
                    dp[i+1][l] = (dp[i+1][l]+dp[i][l])%MOD 
            cnt = (dp[-1][k]-prev)%MOD
            result = (result+mn*cnt)%MOD
            prev = dp[-1][k]
        return result


# Time:  O(n^3 * len(diffs)) = O(n^5) at most
import collections
from functools import reduce


# sort, dp
class Solution2(object):
    def sumOfPowers(self, nums, k):
        MOD = 10**9+7
        nums.sort()
        dp = [[collections.defaultdict(int) for _ in range(len(nums)+1)] for _ in range(len(nums))]        
        for i in range(len(nums)):
            for j in range(max(k-(len(nums)-i+1)-1, 0), i):
                diff = nums[i]-nums[j]
                dp[i][2][diff] += 1
                for l in range(max(k-(len(nums)-i+1), 0), i+1):
                    for mn, cnt in dp[j][l].items():
                        dp[i][l+1][min(diff, mn)] = (dp[i][l+1][min(diff, mn)]+cnt)%MOD
        return reduce(lambda accu, x: (accu+x)%MOD, ((mn*cnt)%MOD for i in range(k-1, len(dp)) for mn, cnt in dp[i][k].items()))
