# Time:  O(n)

class Solution(object):
    def averageWaitingTime(self, customers):
        
        avai = wait = 0.0
        for a, t in customers:
            avai = max(avai, a)+t
            wait += avai-a
        return wait/len(customers)
