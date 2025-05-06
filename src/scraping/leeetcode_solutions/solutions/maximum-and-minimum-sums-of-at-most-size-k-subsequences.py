from functools import reduce
# Time:  O(nlogn)

# sort, combinatorics, two pointers, sliding window
MOD = 10**9+7
FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
def nCr(n, k):
    if n < k:
        return 0
    while len(INV) <= n:  # lazy initialization
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)
    return (FACT[n]*INV_FACT[n-k] % MOD) * INV_FACT[k] % MOD


class Solution(object):
    def minMaxSums(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        nums.sort()
        result = 0
        cnt = 1
        for i in range(len(nums)):
            result = (result+(nums[i]+nums[~i])*cnt)%MOD
            cnt = (cnt*2-nCr(i, k-1)) % MOD
        return result


# Time:  O(nlogn + n * k)
# sort, combinatorics
class Solution2(object):
    def minMaxSums(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        nums.sort()
        result = 0
        cnt = 1
        for i in range(len(nums)):
            cnt = reduce(lambda accu, x: (accu+x)%MOD, (nCr(i, j) for j in range(min(i, k-1)+1)), 0)
            result = (result+(nums[i]+nums[~i])*cnt)%MOD
        return result
