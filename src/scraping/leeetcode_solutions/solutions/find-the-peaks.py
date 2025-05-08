# Time:  O(n)

# array
class Solution(object):
    def findPeaks(self, mountain):
        
        return [i for i in range(1, len(mountain)-1) if mountain[i-1] < mountain[i] > mountain[i+1]]
