# Time:  O(n)

class Solution(object):
    def findMaxAverage(self, nums, k):
        
        result = total = sum(nums[:k])
        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            result = max(result, total)
        return float(result) / k

