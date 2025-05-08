# Time:  O(nlogn)

# sort, greedy
class Solution(object):
    def minimizeSum(self, nums):
        
        nums.sort()
        return min(nums[-3+i]-nums[i] for i in range(3))
