# Time:  O(n)

# two pointers
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        result = left = total = 0
        lookup = set()
        for right in range(len(nums)):
            while nums[right] in lookup or len(lookup) == k:
                lookup.remove(nums[left])
                total -= nums[left]
                left += 1
            lookup.add(nums[right])
            total += nums[right]
            if len(lookup) == k:
                result = max(result, total)
        return result
