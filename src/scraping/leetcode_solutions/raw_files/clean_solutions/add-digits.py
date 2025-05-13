# Time:  O(1)

class Solution(object):
    def addDigits(self, num):
        return (num - 1) % 9 + 1 if num > 0 else 0

