# Time:  O(n)
# Space: O(1)

# constructive algorithms, math
class Solution(object):
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        """
        :type nums: List[int]
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        MOD = 10**9+7

        n = len(nums)
        mx = max(nums)
        total = mx*n-sum(nums)

        if n <= 2 or cost1*2 <= cost2:
            return total*cost1%MOD
    
        result = float("inf")
        mn = min(nums)
        cnt1 = max((mx-mn)-(total-(mx-mn)), 0)
        cnt2 = total-cnt1
        result = min(result, (cnt1+cnt2%2)*cost1 + cnt2//2*cost2)

        x, cnt1 = divmod(cnt1, (n-2))
        total += n*x
        cnt2 = total-cnt1
        result = min(result, (cnt1+cnt2%2)*cost1 + (cnt2//2)*cost2)

        for _ in range(2):  # increase twice is for odd n
            total += n
            result = min(result, total%2*cost1 + total//2*cost2)
        return result%MOD
