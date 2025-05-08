# Time:  O(n)

# combinatorics
class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        
        MOD = 10**9+7
        result, prev = 1, -1
        for i in range(len(nums)):
            if nums[i] != 1:
                continue
            if prev != -1:
                result = (result*(i-prev))%MOD
            prev = i
        return result if prev != -1 else 0
