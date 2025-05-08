# Time:  O(n)

# string
class Solution(object):
    def getEncryptedString(self, s, k):
        
        return "".join(s[(i+k)%len(s)] for i in range(len(s)))
