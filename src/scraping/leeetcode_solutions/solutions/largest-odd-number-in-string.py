# Time:  O(n)

class Solution(object):
    def largestOddNumber(self, num):
        
        for i in reversed(range(len(num))):
            if int(num[i])%2:
                return num[:i+1]
        return ""
