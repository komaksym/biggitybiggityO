# Time:  O(n)

# sliding window, two pointers
class Solution(object):
    def countSubarrays(self, nums, k):
        result = total = left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total*(right-left+1) >= k:
                total -= nums[left]
                left += 1
            result += right-left+1
        return result
