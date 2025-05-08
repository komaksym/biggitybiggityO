# Time:  O(n)

# combinatorics
class Solution(object):
    def countSubstrings(self, s, c):
        
        n = s.count(c)
        return (n+1)*n//2
