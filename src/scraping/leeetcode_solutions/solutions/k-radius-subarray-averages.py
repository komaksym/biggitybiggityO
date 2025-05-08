# Time:  O(n)

class Solution(object):
    def getAverages(self, nums, k):
        
        total, l = 0, 2*k+1
        result = [-1]*len(nums)
        for i in range(len(nums)):
            total += nums[i]
            if i-l >= 0:
                total -= nums[i-l]
            if i >= l-1:
                result[i-k] = total//l
        return result
