# Time:  O(n)

# array, greedy
class Solution(object):
    def minimumSwaps(self, nums):
        min_idx = min(range(len(nums)), key=nums.__getitem__)
        max_idx = max(reversed(range(len(nums))), key=nums.__getitem__)
        return ((len(nums)-1)-max_idx)+min_idx-int(max_idx < min_idx)
