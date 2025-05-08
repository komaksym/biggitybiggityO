# Time:  O(nlogn)

class Solution(object):
    def getMaximumConsecutive(self, coins):
        coins.sort()
        result = 1
        for c in coins:
            if c > result:
                break
            result += c
        return result
