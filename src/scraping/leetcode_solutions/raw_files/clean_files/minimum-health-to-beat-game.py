# Time:  O(n)

# greedy
class Solution(object):
    def minimumHealth(self, damage, armor):
        return sum(damage)-min(max(damage), armor)+1
