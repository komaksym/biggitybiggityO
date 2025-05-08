# Time:  O(n)

# array, two pointers
class Solution(object):
    def captureForts(self, forts):
        
        result = left = 0
        for right in range(len(forts)):
            if not forts[right]:
                continue
            if forts[right] == -forts[left]:
                result = max(result, right-left-1)
            left = right
        return result
