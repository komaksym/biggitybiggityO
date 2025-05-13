# Time:  O(n)

class Solution(object):
    def minStartValue(self, nums):
        min_prefix, prefix = 0, 0
        for num in nums:
            prefix += num
            min_prefix = min(min_prefix, prefix)
        return 1-min_prefix
