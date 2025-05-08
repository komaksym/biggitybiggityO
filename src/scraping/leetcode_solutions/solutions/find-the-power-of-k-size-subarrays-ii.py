# Time:  O(n)

# two pointers, sliding window
class Solution(object):
    def resultsArray(self, nums, k):
        
        result = [-1]*(len(nums)-k+1)
        left = 0
        for right in range(len(nums)):
            if nums[right]-nums[left] != right-left:
                left = right
            if right-left+1 == k:
                result[left] = nums[right]
                left += 1
        return result
