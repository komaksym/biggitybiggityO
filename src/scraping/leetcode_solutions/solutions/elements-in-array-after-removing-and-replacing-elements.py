# Time:  O(n)

class Solution(object):
    def elementInNums(self, nums, queries):
        
        result = []
        for t, i in queries:
            t %= 2*len(nums)
            if t+i < len(nums):
                result.append(nums[t+i])
            elif i < t-len(nums):
                result.append(nums[i])
            else:
                result.append(-1)
        return result
