# Time:  O(n * (logb + logc))

# fast exponentiation
class Solution(object):
    def getGoodIndices(self, variables, target):
        return [i for i, (a, b, c, m) in enumerate(variables) if pow(pow(a, b, 10), c, m) == target]
