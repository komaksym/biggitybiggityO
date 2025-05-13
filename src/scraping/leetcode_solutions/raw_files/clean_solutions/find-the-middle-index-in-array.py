# Time:  O(n)

class Solution(object):
    def findMiddleIndex(self, nums):
        total = sum(nums)
        accu = 0
        for i, x in enumerate(nums):
            if accu*2 == total-x:
                return i
            accu += x
        return -1
