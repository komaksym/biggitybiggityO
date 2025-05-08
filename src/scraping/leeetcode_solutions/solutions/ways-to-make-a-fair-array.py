# Time:  O(n)

class Solution(object):
    def waysToMakeFair(self, nums):
        
        prefix = [0]*2
        suffix = [sum(nums[i] for i in range(k, len(nums), 2)) for k in range(2)]
        result = 0
        for i, num in enumerate(nums):
            suffix[i%2] -= num
            result += int(prefix[0]+suffix[1] == prefix[1]+suffix[0])
            prefix[i%2] += num
        return result
