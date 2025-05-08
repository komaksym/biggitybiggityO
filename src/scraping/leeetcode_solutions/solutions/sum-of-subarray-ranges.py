# Time:  O(n)

class Solution(object):
    def subArrayRanges(self, nums):
        
        result = 0
        stk = []
        for i in range(len(nums)+1):
            x = nums[i] if i < len(nums) else float("inf")
            while stk and nums[stk[-1]] <= x:
                j = stk.pop()
                k = stk[-1] if stk else -1
                result += nums[j]*(j-k)*(i-j)
            stk.append(i)
        stk = []
        for i in range(len(nums)+1):
            x = nums[i] if i < len(nums) else float("-inf")
            while stk and nums[stk[-1]] >= x:
                j = stk.pop()
                k = stk[-1] if stk else -1
                result -= nums[j]*(j-k)*(i-j)
            stk.append(i)
        return result
