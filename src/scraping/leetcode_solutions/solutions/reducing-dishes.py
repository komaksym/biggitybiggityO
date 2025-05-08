# Time:  O(nlogn)

class Solution(object):
    def maxSatisfaction(self, satisfaction):
        
        satisfaction.sort(reverse=True)
        result, curr = 0, 0
        for x in satisfaction:
            curr += x
            if curr <= 0:
                break
            result += curr
        return result
