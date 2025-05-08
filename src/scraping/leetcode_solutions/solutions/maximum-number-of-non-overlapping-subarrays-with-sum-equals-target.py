# Time:  O(n)

class Solution(object):
    def maxNonOverlapping(self, nums, target):
        
        lookup = {0:-1}
        result, accu, right = 0, 0, -1
        for i, num in enumerate(nums):
            accu += num
            if accu-target in lookup and lookup[accu-target] >= right:
                right = i
                result += 1 
            lookup[accu] = i
        return result
