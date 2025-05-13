# Time:  O(n)

class Solution(object):
    def sumOfBeauties(self, nums):
        right = [nums[-1]]*len(nums)
        for i in reversed(range(2, len(nums)-1)):
            right[i] = min(right[i+1], nums[i])
        result, left = 0, nums[0]
        for i in range(1, len(nums)-1):
            if left < nums[i] < right[i+1]:
                result += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                result += 1
            left = max(left, nums[i])
        return result
