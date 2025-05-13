# Time:  O(n)

# greedy, sliding window
class Solution(object):
    def checkArray(self, nums, k):
        curr = 0
        for i, x in enumerate(nums):
            if x-curr < 0:
                return False
            nums[i] -= curr
            curr += nums[i]
            if i-(k-1) >= 0:
                curr -= nums[i-(k-1)]
        return curr == 0
