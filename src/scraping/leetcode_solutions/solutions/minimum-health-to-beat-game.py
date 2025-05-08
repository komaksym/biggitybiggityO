# Time:  O(n)

# greedy
class Solution(object):
    def minimumHealth(self, damage, armor):
        """
        :type damage: List[int]
        :type armor: int
        :rtype: int
        """
        return sum(damage)-min(max(damage), armor)+1
