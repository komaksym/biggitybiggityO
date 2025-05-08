# Time:  O(n)

# greedy
class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        result = parity = 0
        diff = float("inf")
        for x in nums:
            y = x^k
            result += max(x, y)
            parity ^= int(x < y)
            diff = min(diff, abs(x-y))
        return result-parity*diff
