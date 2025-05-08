# Time:  O(n)

# prefix sum
class Solution(object):
    def leftRigthDifference(self, nums):
        
        total = sum(nums)
        result = []
        curr = 0
        for x in nums:
            curr += x
            result.append(abs((curr-x)-(total-curr)))
        return result
