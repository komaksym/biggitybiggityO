# Time:  O(1)
# Space: O(1)

class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0


class Solution2(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & ~-n) == 0

