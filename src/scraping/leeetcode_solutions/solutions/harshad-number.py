# Time:  O(logx)

# math
class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        
        result = 0
        y = x
        while y:
            y, r = divmod(y, 10)
            result += r
        return result if x%result == 0 else -1
