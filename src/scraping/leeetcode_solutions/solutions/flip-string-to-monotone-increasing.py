# Time:  O(n)

class Solution(object):
    def minFlipsMonoIncr(self, S):
        
        flip0, flip1 = 0, 0
        for c in S:
            flip0 += int(c == '1')
            flip1 = min(flip0, flip1 + int(c == '0'))
        return flip1
