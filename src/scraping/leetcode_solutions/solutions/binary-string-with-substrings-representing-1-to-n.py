# Time:  O(n^2), n is the length of S
# Space: O(1)

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        return all(bin(i)[2:] in S for i in reversed(range(N//2, N+1)))
