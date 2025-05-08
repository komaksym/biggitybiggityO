# Time:  O(logn/logm), n is numBottles, m is numExchange

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        result = numBottles
        while numBottles >= numExchange:
            numBottles, remainder = divmod(numBottles, numExchange)
            result += numBottles
            numBottles += remainder
        return result
