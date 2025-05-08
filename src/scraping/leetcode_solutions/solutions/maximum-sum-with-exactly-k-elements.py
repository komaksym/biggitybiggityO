# Time:  O(n)

# math
class Solution(object):
    def maximizeSum(self, nums, k):
        
        return max(nums)*k+k*(k-1)//2
