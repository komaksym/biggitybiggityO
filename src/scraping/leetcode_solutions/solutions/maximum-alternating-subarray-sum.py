# Time:  O(n)

class Solution(object):
    def maximumAlternatingSubarraySum(self, nums):
        def kadane(nums, start):
            result = float("-inf")
            curr = odd = 0
            for i in range(start, len(nums)):
                curr = (curr+nums[i]) if not odd else max(curr-nums[i], 0)
                result = max(result, curr)
                odd ^= 1
            return result

        return max(kadane(nums, 0), kadane(nums, 1))
