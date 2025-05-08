# Time:  O(nlogn)

# sort, prefix sum, greedy
class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        prefix = sum(nums)
        for i in reversed(range(2, len(nums))):
            prefix -= nums[i]
            if prefix > nums[i]:
                return prefix+nums[i]
        return -1
