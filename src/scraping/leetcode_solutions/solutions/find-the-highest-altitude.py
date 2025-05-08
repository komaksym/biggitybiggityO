# Time:  O(n)

class Solution(object):
    def largestAltitude(self, gain):
        
        result = curr = 0
        for g in gain:
            curr += g
            result = max(result, curr)
        return result
