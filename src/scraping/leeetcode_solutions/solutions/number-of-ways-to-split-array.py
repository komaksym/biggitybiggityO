# Time:  O(n)

# prefix sum
class Solution(object):
    def waysToSplitArray(self, nums):
        
        total = sum(nums)
        result = curr = 0
        for i in range(len(nums)-1):
            curr += nums[i]
            result += int(curr >= total-curr)
        return result
