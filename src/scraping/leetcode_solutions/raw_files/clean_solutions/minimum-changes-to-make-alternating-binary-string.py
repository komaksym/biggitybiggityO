# Time:  O(n)

class Solution(object):
    def minOperations(self, s):
        cnt = sum(int(c) == i%2 for i, c in enumerate(s))
        return min(cnt, len(s)-cnt)
