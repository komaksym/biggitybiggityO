# Time:  O(n)

# dp
class Solution(object):
    def countAlternatingSubarrays(self, nums):
        result = curr = 0
        for i in range(len(nums)):
            if i-1 >= 0 and nums[i-1] == nums[i]:
                curr = 0
            curr += 1
            result += curr
        return result
