# Time:  O(n)

class Solution(object):
    def minFlips(self, target):
        
        result, curr = 0, '0'
        for c in target:
            if c == curr:
                continue
            curr = c
            result += 1
        return result
