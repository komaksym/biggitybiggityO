# Time:  O(1)

# greedy, math
class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        return min(numOnes, k)-max(k-numOnes-numZeros, 0)
