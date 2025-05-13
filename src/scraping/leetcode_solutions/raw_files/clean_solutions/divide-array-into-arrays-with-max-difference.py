# Time:  O(nlogn)

# sort
class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        return [nums[i:i+3] for i in range(0, len(nums), 3)] if all(nums[i+2]-nums[i] <= k for i in range(0, len(nums), 3)) else []
