# Time:  O(n)

# math
class Solution(object):
    def averageValue(self, nums):
        total = cnt = 0
        for x in nums:
            if x%6:
                continue
            total += x
            cnt += 1
        return total//cnt if cnt else 0
