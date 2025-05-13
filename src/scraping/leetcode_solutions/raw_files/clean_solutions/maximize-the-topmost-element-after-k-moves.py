# Time:  O(min(n, k))

# constructive algorithms
class Solution(object):
    def maximumTop(self, nums, k):
        if len(nums) == 1 == k%2:
            return -1
        if k <= 1:
            return nums[k]
        return max(nums[i] for i in range(min(k+1, len(nums))) if i != k-1)
