# Time:  O(n)

# greedy
class Solution(object):
    def minimumCost(self, s):
        return sum(min(i+1, len(s)-(i+1)) for i in range(len(s)-1) if s[i] != s[i+1])
