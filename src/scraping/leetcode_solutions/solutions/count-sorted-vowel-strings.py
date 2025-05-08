# Time:  O(1)
# Space: O(1)

class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        def nCr(n, r): 
            if n-r < r:
                return nCr(n, n-r)
            c = 1
            for k in range(1, r+1):
                c *= n-k+1
                c //= k
            return c
    
        return nCr(n+4, 4) 
