# Time:  O(nlogn)

# sort, greedy
class Solution(object):
    def minDamage(self, power, damage, health):
        """
        :type power: int
        :type damage: List[int]
        :type health: List[int]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
        
        idxs = list(range(len(health)))
        idxs.sort(key=lambda i: float(ceil_divide(health[i], power))/damage[i])
        result = t = 0
        for i in idxs:
            t += ceil_divide(health[i], power)
            result += t*damage[i]
        return result
