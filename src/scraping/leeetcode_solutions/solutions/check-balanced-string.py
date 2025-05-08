# Time:  O(n)

# string
class Solution(object):
    def isBalanced(self, num):
        
        return sum(ord(num[i])-ord('0') for i in range(0, len(num), 2)) == sum(ord(num[i])-ord('0') for i in range(1, len(num), 2))
