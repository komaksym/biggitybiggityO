# Time:  O(nlogn)

# sort, two pointers, sliding window
class Solution(object):
    def maximumBeauty(self, nums, k):
        
        nums.sort()
        left = 0
        for right in range(len(nums)):
            if nums[right]-nums[left] > k*2:
                left += 1
        return right-left+1
