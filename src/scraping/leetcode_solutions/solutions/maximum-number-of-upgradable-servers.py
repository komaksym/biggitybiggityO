# Time:  O(n)

import itertools


# math
class Solution(object):
    def maxUpgrades(self, count, upgrade, sell, money):
        """
        :type count: List[int]
        :type upgrade: List[int]
        :type sell: List[int]
        :type money: List[int]
        :rtype: List[int]
        """
        return [min(c+(m-c*u)//(u+s), c) for c, u, s, m in zip(count, upgrade, sell, money)]
