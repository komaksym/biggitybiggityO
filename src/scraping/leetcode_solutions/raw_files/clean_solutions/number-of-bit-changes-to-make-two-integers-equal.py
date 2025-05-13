# Time:  O(logn)

# bit manipulation
class Solution(object):
    def minChanges(self, n, k):
        def popcount(x):
            return bin(x).count('1')

        return popcount(n^k) if n&k == k else -1


# Time:  O(logn)
# bit manipulation
class Solution2(object):
    def minChanges(self, n, k):
        def popcount(x):
            return bin(x).count('1')

        return popcount(n^k) if n|(n^k) == n else -1
