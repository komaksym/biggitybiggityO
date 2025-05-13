# Time:  O(n)

class Solution(object):
    def numTimesAllBlue(self, light):
        result, right = 0, 0
        for i, num in enumerate(light, 1):
            right = max(right, num)
            result += (right == i)
        return result
