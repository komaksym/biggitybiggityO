# Time:  O(n)

class Solution(object):
    def nextGreaterElements(self, nums):
        
        result, stk = [0] * len(nums), []
        for i in reversed(range(2*len(nums))):
            while stk and stk[-1] <= nums[i % len(nums)]:
                stk.pop()
            result[i % len(nums)] = stk[-1] if stk else -1
            stk.append(nums[i % len(nums)])
        return result

