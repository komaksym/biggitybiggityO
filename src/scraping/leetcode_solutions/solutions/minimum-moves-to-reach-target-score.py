# Time:  O(logn)

# greedy
class Solution(object):
    def minMoves(self, target, maxDoubles):
        
        result = 0
        while target > 1 and maxDoubles:
            result += 1+target%2
            target //= 2
            maxDoubles -= 1
        return result+(target-1)
