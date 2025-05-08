# Time:  O(nlogn + r^2), r = max(rewardValues)

# sort, dp, bitset
class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        mx = max(rewardValues)
        dp = 1
        mask = (1<<mx)-1
        for v in sorted(set(rewardValues)):
            x = dp&((1<<v)-1)
            dp |= (x<<v)&mask
        return mx+(dp.bit_length()-1)


# Time:  O(nlogn + r^2), r = max(rewardValues)
# sort, dp, bitset
class Solution2(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        dp = 1
        for v in sorted(set(rewardValues)):
            x = dp&((1<<v)-1)
            dp |= x<<v
        return dp.bit_length()-1


# Time:  O(nlogn + r^2), r = max(rewardValues)
# sort, dp
class Solution3(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        mx = max(rewardValues)
        dp = [False]*((mx-1)+1)
        dp[0] = True
        for v in sorted(set(rewardValues)):
            for x in range(min(v, mx-v)):
                dp[x+v] |= dp[x]
        return mx+next(x for x in reversed(range(len(dp))) if dp[x])


# Time:  O(nlogn + r^2), r = max(rewardValues)
# sort, dp
class Solution4(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        dp = [False]*((max(rewardValues)*2-1)+1)
        dp[0] = True
        for v in sorted(set(rewardValues)):
            for x in range(v):
                dp[x+v] |= dp[x]
        return next(x for x in reversed(range(len(dp))) if dp[x])
