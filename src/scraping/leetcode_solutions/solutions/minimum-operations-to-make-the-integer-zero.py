# Time:  O(1)

# math, linear search, bit manipulations
class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        def popcount(x):
            result = 0
            while x:
                x &= (x-1)
                result += 1
            return result

        for i in range(1, 60+1):
            if num1-i*num2 < 0:
                break
            if popcount(num1-i*num2) <= i <= num1-i*num2:
                return i
        return -1
