# Time:  O(nlogn)

# sort
class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
