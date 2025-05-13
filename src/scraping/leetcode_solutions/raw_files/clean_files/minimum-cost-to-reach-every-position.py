# Time:  O(n)

# prefix sum
class Solution(object):
    def minCosts(self, cost):
        for i in range(1, len(cost)):
            cost[i] = min(cost[i], cost[i-1])
        return cost
