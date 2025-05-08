# Time:  O(n)

# two pointers, combinatorics
class Solution(object):
    def zeroFilledSubarray(self, nums):
        result = 0
        prev = -1
        for i in range(len(nums)):
            if nums[i]:
                prev = i
                continue
            result += i-prev
        return result
