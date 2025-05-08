# Time:  O(n)

# prefix sum
class Solution(object):
    def findPrefixScore(self, nums):
        
        curr = 0
        for i in range(len(nums)):
            curr = max(curr, nums[i])
            nums[i] += (nums[i-1] if i-1 >= 0 else 0)+curr
        return nums
