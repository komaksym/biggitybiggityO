# Time:  O(nlogn)

class Solution(object):
    def numSubseq(self, nums, target):
        
        MOD = 10**9 + 7
        nums.sort()
        result = 0
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left]+nums[right] > target:
                right -= 1
            else:
                result = (result+pow(2, right-left, MOD))%MOD
                left += 1
        return result
