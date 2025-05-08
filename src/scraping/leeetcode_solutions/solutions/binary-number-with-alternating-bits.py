# Time:  O(1)

class Solution(object):
    def hasAlternatingBits(self, n):
        
        n, curr = divmod(n, 2)
        while n > 0:
            if curr == n % 2:
                return False
            n, curr = divmod(n, 2)
        return True

