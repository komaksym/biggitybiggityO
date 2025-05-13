# Time:  O(nlogn)

# sort
class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        return min((nums[i]+nums[~i])/2.0 for i in range(len(nums)//2))
