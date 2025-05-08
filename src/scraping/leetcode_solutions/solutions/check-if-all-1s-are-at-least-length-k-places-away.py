# Time:  O(n)

class Solution(object):
    def kLengthApart(self, nums, k):
        prev = -k-1
        for i in range(len(nums)):
            if not nums[i]:
                continue
            if i-prev <= k:
                return False
            prev = i
        return True
