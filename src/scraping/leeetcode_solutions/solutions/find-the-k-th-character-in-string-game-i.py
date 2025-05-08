# Time:  O(1)

# bitmasks
class Solution(object):
    def kthCharacter(self, k):
        
        def popcount(x):
            return bin(x)[2:].count('1')

        return chr(ord('a')+popcount(k-1)%26)
