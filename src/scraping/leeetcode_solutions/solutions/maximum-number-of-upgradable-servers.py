# Time:  O(n)

import itertools


# math
class Solution(object):
    def maxUpgrades(self, count, upgrade, sell, money):
        
       
       
       
       
        return [min(c+(m-c*u)//(u+s), c) for c, u, s, m in zip(count, upgrade, sell, money)]
