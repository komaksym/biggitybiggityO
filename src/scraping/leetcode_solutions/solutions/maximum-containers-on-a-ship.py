# Time:  O(1)

# math
class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        
        return min(maxWeight//w, n*n)
