# Time:  O(n)

# mono stack
class Solution(object):
    def maximumLengthOfRanges(self, nums):
        
        result = [0]*len(nums)
        stk = [-1]
        nums.append(float("inf"))
        for i, x in enumerate(nums):
            while stk[-1] != -1 and nums[stk[-1]] < x:
                j = stk.pop()
                result[j] = (i-1)-stk[-1]
            stk.append(i)
        return result
