# Time:  O(k)

class Solution(object):
    def smallestRepunitDivByK(self, K):
        if K % 2 == 0 or K % 5 == 0:
            return -1

        result = 0
        for N in range(1, K+1):
            result = (result*10+1) % K
            if not result:
                return N
        assert(False)
        return -1 
