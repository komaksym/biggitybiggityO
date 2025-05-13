# Time:  O(n)

class Solution(object):
    def countOdds(self, low, high):
        return (high+1)//2 - ((low-1)+1)//2
