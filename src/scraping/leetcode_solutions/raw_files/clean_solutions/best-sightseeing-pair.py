# Time:  O(n)

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        result, curr = 0, 0
        for x in A:
            result = max(result, curr+x)
            curr = max(curr, x)-1
        return result
