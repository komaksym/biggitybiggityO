# Time:  O(n)

# two pointers
class Solution(object):
    def incremovableSubarrayCount(self, nums):
        for j in reversed(range(1, len(nums))):
            if not nums[j-1] < nums[j]:
                break
        else:
            return (len(nums)+1)*len(nums)//2
        result = len(nums)-j+1
        for i in range(len(nums)-1):
            while j < len(nums) and not (nums[i] < nums[j]):
                j += 1
            result += len(nums)-j+1
            if not (nums[i] < nums[i+1]):
                break
        return result
