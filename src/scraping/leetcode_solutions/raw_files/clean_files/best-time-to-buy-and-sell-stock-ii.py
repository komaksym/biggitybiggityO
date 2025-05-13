# Time:  O(n)


class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

    def maxProfit2(self, prices):
        return sum([max(prices[x + 1] - prices[x], 0) for x in range(len(prices[:-1]))])

