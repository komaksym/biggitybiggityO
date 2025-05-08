# Time:  O(n)

class Solution(object):
    def maxScore(self, s):
        result, zeros, ones = 0, 0, 0
        for i in range(1, len(s)-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            result = max(result, zeros-ones)
        return result + ones + (s[0] == '0') + (s[-1] == '1')
