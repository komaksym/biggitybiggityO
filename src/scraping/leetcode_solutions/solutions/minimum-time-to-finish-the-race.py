# Time:  O((n + l) * logc)

# greedy, dp
class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        
        def ceil_log2(x):
            return (x-1).bit_length()

        dp = [float("inf")]*ceil_log2(changeTime+1) 
        for f, r in tires:
            total = curr = f
            cnt = 0
            while curr < changeTime+f: 
                dp[cnt] = min(dp[cnt], total)
                curr *= r
                total += curr
                cnt += 1
        dp2 = [float("inf")]*numLaps 
        for i in range(numLaps):
            dp2[i] = min((dp2[i-j-1]+changeTime if i-j-1 >= 0 else 0)+dp[j] for j in range(min(i+1, len(dp))))
        return dp2[-1]
