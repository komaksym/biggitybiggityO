# Time:  O(n^2), n is the length of S

class Solution(object):
    def queryString(self, S, N):
        return all(bin(i)[2:] in S for i in reversed(range(N//2, N+1)))
