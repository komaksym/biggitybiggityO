# Time:  O(n)

# sliding window, two pointers
class Solution(object):
    def longestNiceSubarray(self, nums):
        result = left = curr = 0
        for right in range(len(nums)):
            while curr&nums[right]:
                curr ^= nums[left]
                left += 1
            curr |= nums[right]
            result = max(result, right-left+1)
        return result
