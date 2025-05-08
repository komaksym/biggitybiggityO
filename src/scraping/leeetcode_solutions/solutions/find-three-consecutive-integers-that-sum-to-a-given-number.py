# Time:  O(1)

# math
class Solution(object):
    def sumOfThree(self, num):
        
        return [num//3-1, num//3, num//3+1] if num%3 == 0 else []
