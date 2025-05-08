# Time:  O(n)

# greedy, constructive algorithms
class Solution(object):
    def minimumMoney(self, transactions):
        
        return sum(max(a-b, 0) for a, b in transactions)+max(a-max(a-b, 0) for a, b in transactions) 
