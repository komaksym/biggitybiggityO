# Time:  O(logn)

class Solution(object):
    def brokenCalc(self, X, Y):
        result = 0
        while X < Y:
            if Y%2:
                Y += 1
            else:
                Y /= 2
            result += 1
        return result + X-Y
