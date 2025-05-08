# Time:  O(n + c^2)

import itertools
import re


# The best theory solution (DP, O(n + c^2)) could be seen here:
# https://leetcode.com/problems/flip-game-ii/discuss/73954/theory-matters-from-backtracking128ms-to-dp-0ms
class Solution(object):
    def canWin(self, s):
        g, g_final = [0], 0
        for p in map(len, re.split('-+', s)):
            while len(g) <= p:
                g += min(set(range(p)) - {x^y for x, y in zip(g[:len(g)/2], g[-2:-len(g)/2-2:-1])}),
            g_final ^= g[p]
        return g_final > 0 


# Time:  O(n + c^3 * 2^c * logc), n is length of string, c is count of "++"
# hash solution.
# We have total O(2^c) game strings,
# and each hash key in hash table would cost O(c),
# each one has O(c) choices to the next one,
# and each one would cost O(clogc) to sort,
# so we get O((c * 2^c) * (c * clogc)) = O(c^3 * 2^c * logc) time.
# To cache the results of all combinations, thus O(c * 2^c) space.
class Solution2(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {}

        def canWinHelper(consecutives):                                        
            consecutives = tuple(sorted(c for c in consecutives if c >= 2))    
            if consecutives not in lookup:
                lookup[consecutives] = any(not canWinHelper(consecutives[:i] + (j, c-2-j) + consecutives[i+1:]) 
                                           for i, c in enumerate(consecutives) 
                                           for j in range(c - 1))             
            return lookup[consecutives]                                        

        return canWinHelper(list(map(len, re.findall(r'\+\++', s))))


# Time:  O(c * n * c!), n is length of string, c is count of "++"
#                  Besides, it costs n space for modifying string at each depth.
class Solution3(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s) - 1
        is_win = False
        while not is_win and i < n:                                    
            if s[i] == '+':
                while not is_win and i < n and s[i+1] == '+':          
                    is_win = not self.canWin(s[:i] + '--' + s[i+2:])   
                    i += 1
            i += 1
        return is_win

