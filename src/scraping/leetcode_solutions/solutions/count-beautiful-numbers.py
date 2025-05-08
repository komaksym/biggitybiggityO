# Time:  O(logr * 2 * 10 * s)

import collections


# dp
class Solution(object):
    def beautifulNumbers(self, l, r):
        
        def count(x):
            s = [ord(x)-ord('0') for x in str(x)]
            dp = [collections.defaultdict(int) for _ in range(2)]
            dp[1][1, 0] = 1
            for c in s:
                new_dp = [collections.defaultdict(int) for _ in range(2)]
                for b in range(2):
                    for (mul, total), cnt in dp[b].items():
                        for x in range((c if b else 9)+1):
                            new_dp[b and x == c][mul*(1 if total == 0 == x else x), total+x] += cnt
                dp = new_dp
            result = 0
            for b in range(2):
                for (mul, total), cnt in dp[b].items():
                    if total and mul%total == 0:
                        result += cnt
            return result

        return count(r)-count(l-1)
