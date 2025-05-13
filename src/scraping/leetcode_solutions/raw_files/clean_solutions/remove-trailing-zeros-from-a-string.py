# Time:  O(n)

# string
class Solution(object):
    def removeTrailingZeros(self, num):
        return num[:next(i for i in reversed(range(len(num))) if num[i] != '0')+1]
