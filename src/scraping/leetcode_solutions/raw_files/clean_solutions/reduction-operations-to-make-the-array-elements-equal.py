# Time:  O(nlogn)

class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        result = curr = 0
        for i in range(1, len(nums)): 
            if nums[i-1] < nums[i]:
                curr += 1
            result += curr
        return result
