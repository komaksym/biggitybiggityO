from functools import reduce
# Time:  O(n)

# greedy
class Solution(object):
    def maxStrength(self, nums):
        if all(x <= 0 for x in nums) and sum(x < 0 for x in nums) <= 1:
            return max(nums)
        result = reduce(lambda x, y: x*y, (x for x in nums if x))
        return result if result > 0 else result//max(x for x in nums if x < 0)
