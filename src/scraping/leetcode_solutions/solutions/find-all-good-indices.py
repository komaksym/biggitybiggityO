# Time:  O(n)

# prefix sum
class Solution(object):
    def goodIndices(self, nums, k):
        left = [1]*len(nums)
        for i in range(1, len(nums)-1):
            if nums[i] <= nums[i-1]:
                left[i] = left[i-1]+1
        right = [1]*len(nums)
        for i in reversed(range(1, len(nums)-1)):
            if nums[i] <= nums[i+1]:
                right[i] = right[i+1]+1
        return [i for i in range(k, len(nums)-k) if min(left[i-1], right[i+1]) >= k]
