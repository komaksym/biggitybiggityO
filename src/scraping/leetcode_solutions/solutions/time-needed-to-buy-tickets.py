# Time:  O(n)

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        return sum(min(x, tickets[k] if i <= k else tickets[k]-1) for i, x in enumerate(tickets))
