# Time:  O(nlogn)

class Solution(object):
    def maxIceCream(self, costs, coins):
        
        costs.sort()
        for i, c in enumerate(costs):
            coins -= c
            if coins < 0:
                return i
        return len(costs)
