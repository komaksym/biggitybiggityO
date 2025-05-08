# Time:  O(n)

class Solution(object):
    def minSwaps(self, nums):
        
        result = cnt = w = nums.count(1)
        for i in range(len(nums)+(w-1)):
            if i >= w:
                cnt += nums[(i-w)%len(nums)]
            cnt -= nums[i%len(nums)]
            result = min(result, cnt)
        return result
