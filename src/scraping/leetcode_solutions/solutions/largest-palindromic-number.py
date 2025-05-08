# Time:  O(n)

import collections


# freq table, greedy
class Solution(object):
    def largestPalindromic(self, num):
        
        cnt = collections.Counter(num)
        result = []
        for i in reversed(range(10)):
            if not cnt[str(i)]//2 or (i == 0 and not result):
                continue
            for _ in range(cnt[str(i)]//2):
                result.append(str(i))
        result.append(max([k for k, v in cnt.items() if v%2] or [""]))
        for i in reversed(range(len(result)-1)):
            result.append(result[i])
        return "".join(result) or "0"
