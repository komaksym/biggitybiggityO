# Time:  O(m + n)

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        
        stk, lookup = [], {}
        for num in nums:
            while stk and num > stk[-1]:
                lookup[stk.pop()] = num
            stk.append(num)
        while stk:
            lookup[stk.pop()] = -1
        return [lookup[x] for x in findNums]

