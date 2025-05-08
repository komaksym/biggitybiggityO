# Time:  O(n * (n + 26))

# dp, freq table
class Solution(object):
    def minimumSubstringsInPartition(self, s):
        INF = float("inf")
        dp = [INF]*(len(s)+1)
        dp[0] = 0
        for i in range(len(s)):
            cnt = [0]*26
            d = mx = 0
            for j in reversed(range(i+1)):
                k = ord(s[j])-ord('a')
                if cnt[k] == 0:
                    d += 1
                cnt[k] += 1
                mx = max(mx, cnt[k])
                if d*mx == i-j+1:
                    dp[i+1] = min(dp[i+1], dp[j]+1)
        return dp[-1]
