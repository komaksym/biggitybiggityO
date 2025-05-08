# Time:  O(n)

class Solution(object):
    def findGameWinner(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        return n%6 != 1


# Time:  O(n)
class Solution2(object):
    def findGameWinner(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        grundy = [0, 1]  # 0-indexed
        for i in range(2, n):
            grundy[i%2] = (grundy[(i-1)%2]+1)^(grundy[(i-2)%2]+1)  # colon principle, replace the branches by a non-branching stalk of length equal to their nim sum
        return grundy[(n-1)%2] > 0
