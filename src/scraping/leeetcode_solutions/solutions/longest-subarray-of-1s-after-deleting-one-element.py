# Time:  O(n)

class Solution(object):
    def longestSubarray(self, nums):
        
        count, left = 0, 0
        for right in range(len(nums)):
            count += (nums[right] == 0)
            if count >= 2:
                count -= (nums[left] == 0)
                left += 1
        return (right-left+1)-1


# Time:  O(n)
class Solution2(object):
    def longestSubarray(self, nums):
        
        result, count, left = 0, 0, 0
        for right in range(len(nums)):
            count += (nums[right] == 0)
            while count >= 2:
                count -= (nums[left] == 0)
                left += 1
            result = max(result, right-left+1)
        return result-1
