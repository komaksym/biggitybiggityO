# Time:  O(n)

# greedy
class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """
        result = 0
        for i in reversed(range(n//2)):
            result += abs(cost[2*i+1]-cost[2*i+2])
            cost[i] += max(cost[2*i+1], cost[2*i+2])
        return result
