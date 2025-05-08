# Time:  O(n)

# array
class Solution(object):
    def transformArray(self, nums):
        
        cnt = 0
        for x in nums:
            if x%2:
                continue
            nums[cnt] = 0
            cnt += 1
        for i in range(cnt, len(nums)):
            nums[i] = 1
        return nums
