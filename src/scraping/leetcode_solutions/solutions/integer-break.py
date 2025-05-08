# Time:  O(logn), pow is O(logn).

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1


        res = 0
        if n % 3 == 0:           
            res = 3 ** (n // 3)
        elif n % 3 == 2:         
            res = 3 ** (n // 3) * 2
        else:                    
            res = 3 ** (n // 3 - 1) * 4
        return res


# Time:  O(n)
# DP solution.
class Solution2(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1

        res = [0, 1, 2, 3]
        for i in range(4, n + 1):
            res[i % 4] = max(res[(i - 2) % 4] * 2, res[(i - 3) % 4] * 3)
        return res[n % 4]

