# Time:  O(n)

# greedy
class Solution(object):
    def maximumPoints(self, enemyEnergies, currentEnergy):
        mn = min(enemyEnergies)
        return ((currentEnergy-mn)+sum(enemyEnergies))//mn if currentEnergy >= mn else 0
