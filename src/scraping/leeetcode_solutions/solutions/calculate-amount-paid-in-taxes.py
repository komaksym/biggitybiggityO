# Time:  O(n)

# simulation
class Solution(object):
    def calculateTax(self, brackets, income):
        
        result = prev = 0
        for u, p in brackets:
            result += max((min(u, income)-prev)*p/100.0, 0.0)
            prev = u
        return result
