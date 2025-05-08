# Time:  O(n)

# one pass, array
class Solution(object):
    def findNonMinOrMax(self, nums):
        
        mx, mn = float("-inf"), float("inf")
        result = -1
        for x in nums:
            if mn < x < mx:
                return x
            if x < mn:
                result = mn
                mn = x
            if x > mx:
                result = mx
                mx = x
        return result if mn < result < mx else -1


# Time:  O(n)
# array
class Solution2(object):
    def findNonMinOrMax(self, nums):
        
        mx, mn = max(nums), min(nums)
        return next((x for x in nums if x not in (mx, mn)), -1)
