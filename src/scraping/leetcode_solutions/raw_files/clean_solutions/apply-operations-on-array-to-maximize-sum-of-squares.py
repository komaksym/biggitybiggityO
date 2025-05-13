from functools import reduce
# Time:  O(nlogr), r = max(nums)

# bit manipulation, greedy, freq table
class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9+7
        l = max(nums).bit_length()
        cnt = [0]*l
        for i in range(l):
            for x in nums:
                if x&(1<<i):
                    cnt[i] += 1
        return reduce(lambda x, y: (x+y)%MOD, (sum(1<<i for i in range(l) if cnt[i] >= j)**2 for j in range(1, k+1)))
