# Time:  O(n)

# mono stack, dp
class Solution(object):
    def totalSteps(self, nums):
        
        dp = [0]*len(nums) 
        stk = []
        for i in reversed(range(len(nums))):
            while stk and nums[stk[-1]] < nums[i]:
                dp[i] = max(dp[i]+1, dp[stk.pop()])
            stk.append(i)
        return max(dp)


# Time:  O(n)
# mono stack, dp
class Solution2(object):
    def totalSteps(self, nums):
        
        dp = [0]*len(nums) 
        stk = []
        for i in range(len(nums)):
            curr = 0
            while stk and nums[stk[-1]] <= nums[i]:
                curr = max(curr, dp[stk.pop()])
            if stk:
                dp[i] = curr+1
            stk.append(i)
        return max(dp)
