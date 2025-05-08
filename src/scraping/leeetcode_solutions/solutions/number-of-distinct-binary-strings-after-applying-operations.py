# Time:  O(logn)

# combinatorics
class Solution(object):
    def countDistinctStrings(self, s, k):
        
        MOD = 10**9+7
        return pow(2, len(s)-k+1, MOD)
