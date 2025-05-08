# Time:  O(logn)

class Solution(object):
    def convertToTitle(self, n):
        result = []
        while n:
            result += chr((n-1)%26 + ord('A'))
            n = (n-1)//26
        result.reverse()
        return "".join(result)

