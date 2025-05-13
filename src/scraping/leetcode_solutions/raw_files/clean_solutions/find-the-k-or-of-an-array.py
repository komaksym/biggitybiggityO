# Time:  O(nlogr)

# bit manipulation
class Solution(object):
    def findKOr(self, nums, k):
        return sum(1<<i for i in range(max(nums).bit_length()) if sum((x&(1<<i)) != 0 for x in nums) >= k)
