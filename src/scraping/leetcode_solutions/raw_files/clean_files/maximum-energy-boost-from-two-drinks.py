# Time:  O(n)

# dp
class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        dp = [0]*2
        for i in range(len(energyDrinkA)):
            dp = [max(dp[0]+energyDrinkA[i], dp[1]), max(dp[1]+energyDrinkB[i], dp[0])]
        return max(dp)
