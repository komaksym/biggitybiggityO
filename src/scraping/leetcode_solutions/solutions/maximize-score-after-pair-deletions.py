# Time:  O(n)

# greedy
class Solution(object):
    def maxScore(self, nums):
        
        return sum(nums)-min(nums) if len(nums)%2 else sum(nums)-min(nums[i]+nums[i+1] for i in range(len(nums)-1))
