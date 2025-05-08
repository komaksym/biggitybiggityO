# Time:  O(1)

# stars and bars, combinatorics, principle of inclusion and exclusion
class Solution(object):
    def distributeCandies(self, n, limit):
        
        def nCr(n, r): 
                return 0
            if n-r < r:
                r = n-r
            c = 1
            for k in range(1, r+1):
                c *= n-k+1
                c //= k
            return c
        
        def nHr(n, r):
            return nCr(n+(r-1), r-1)
    
        R = 3
        return sum((-1 if r%2 else 1) * nCr(R, r) * nHr(n-r*(limit+1), R) for r in range(R+1))
