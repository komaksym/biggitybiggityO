# Time:  O(n)

# greedy
class Solution(object):
    def buyChoco(self, prices, money):
        i = min(range(len(prices)), key=lambda x: prices[x])
        j = min((j for j in range(len(prices)) if j != i), key=lambda x: prices[x])
        return money-(prices[i]+prices[j]) if prices[i]+prices[j] <= money else money
