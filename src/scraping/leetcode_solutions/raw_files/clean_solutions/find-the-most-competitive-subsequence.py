# Time:  O(n)

class Solution(object):
    def mostCompetitive(self, nums, k):
        stk = []
        for i, x in enumerate(nums):
            while stk and stk[-1] > x and len(stk)+(len(nums)-i) > k:
                stk.pop()
            if len(stk) < k:
                stk.append(x)
        return stk
