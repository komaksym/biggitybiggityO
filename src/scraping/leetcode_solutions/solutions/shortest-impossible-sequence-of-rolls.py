# Time:  O(n)

# constructive algorithms
class Solution(object):
    def shortestSequence(self, rolls, k):
        
        l = 0
        lookup = set()
        for x in rolls:
            lookup.add(x)
            if len(lookup) != k:
                continue
            lookup.clear()
            l += 1
        return l+1
