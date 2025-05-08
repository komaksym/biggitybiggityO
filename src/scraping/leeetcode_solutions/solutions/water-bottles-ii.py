# Time:  O(sqrt(n))

# simulation
class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        
        result = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            numExchange += 1
            result += 1
            numBottles += 1
        return result
