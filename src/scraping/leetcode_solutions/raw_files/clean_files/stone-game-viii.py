from functools import reduce
# Time:  O(n)

class Solution(object):
    def stoneGameVIII(self, stones):
        for i in range(len(stones)-1):
            stones[i+1] += stones[i]
        return reduce(lambda curr, i: max(curr, stones[i]-curr), reversed(range(1, len(stones)-1)), stones[-1])
