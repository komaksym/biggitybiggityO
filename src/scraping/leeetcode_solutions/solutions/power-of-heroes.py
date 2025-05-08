# Time:  O(nlogn)

# sort, combinatorics, dp
class Solution(object):
    def sumOfPower(self, nums):
        
        MOD = 10**9+7
        nums.sort()
        result = dp = 0
        for x in nums:
            result = (result+(x**2)*(dp+x))%MOD
            dp = (dp+(dp+x))%MOD
        return result
