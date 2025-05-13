# Time:  O(n)

# prefix sum
class Solution(object):
    def returnToBoundaryCount(self, nums):
        result = curr = 0
        for x in nums:
            curr += x
            if curr == 0:
                result += 1
        return result
