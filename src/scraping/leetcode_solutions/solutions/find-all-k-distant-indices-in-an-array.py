# Time:  O(n)

# two pointers
class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        result = []
        prev = -1
        for i, x in enumerate(nums):
            if x != key:
                continue
            for j in range(max(i-k, prev+1), min(i+k+1, len(nums))):
                result.append(j)
            prev = min(i+k, len(nums)-1)
        return result
