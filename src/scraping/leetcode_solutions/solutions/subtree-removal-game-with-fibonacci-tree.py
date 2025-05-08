# Time:  O(n)

class Solution(object):
    def findGameWinner(self, n):
        return n%6 != 1


# Time:  O(n)
class Solution2(object):
    def findGameWinner(self, n):
        grundy = [0, 1] 
        for i in range(2, n):
            grundy[i%2] = (grundy[(i-1)%2]+1)^(grundy[(i-2)%2]+1) 
        return grundy[(n-1)%2] > 0
