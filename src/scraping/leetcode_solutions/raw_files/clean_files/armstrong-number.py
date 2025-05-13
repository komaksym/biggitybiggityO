# Time:  O(klogk)

class Solution(object):
    def isArmstrong(self, N):
        n_str = str(N)
        return sum(int(i)**len(n_str) for i in n_str) == N
