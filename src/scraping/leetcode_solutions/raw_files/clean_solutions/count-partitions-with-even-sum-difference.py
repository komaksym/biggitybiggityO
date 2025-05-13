# Time:  O(n)

# prefix sum
class Solution(object):
    def countPartitions(self, nums):
        result = left = 0
        right = sum(nums)
        for i in range(len(nums)-1):
            left += nums[i]
            right -= nums[i]
            if left%2 == right%2:
                result += 1
        return result
