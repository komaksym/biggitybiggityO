# Time:  O(nlogn)

# sort, array
class Solution(object):
    def countWays(self, ranges):
        
        MOD = 10**9+7

        ranges.sort()
        cnt = 0
        curr = float("-inf")
        for l, r in ranges:
            if l > curr:
                cnt += 1
            curr = max(curr, r)
        return pow(2, cnt, MOD)
