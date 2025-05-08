# Time:  O(n^2)

# string
class Solution(object):
    def stringSequence(self, target):
        
        return [target[:i]+chr(x) for i in range(len(target)) for x in range(ord('a'), ord(target[i])+1)]
