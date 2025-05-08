# Time:  O(n)

# prefix sum
class Solution(object):
    def divisibilityArray(self, word, m):
        
        result = []
        curr = 0
        for c in word:
            curr = (curr*10+(ord(c)-ord('0')))%m
            result.append(int(curr == 0))
        return result
