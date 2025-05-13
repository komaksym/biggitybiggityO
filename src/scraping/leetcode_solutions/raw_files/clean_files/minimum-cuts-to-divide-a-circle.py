# Time:  O(1)

# math
class Solution(object):
    def numberOfCuts(self, n):
        return 0 if n == 1 else n if n%2 else n//2
