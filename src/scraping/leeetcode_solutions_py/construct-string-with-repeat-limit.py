# Time:  O(26 * n)
# Space: O(26)

import collections


# greedy
class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        cnt = collections.Counter([ord(x)-ord('a') for x in s])
        result = []
        top1 = 25
        while True:
            top1 = next((i for i in reversed(range(top1+1)) if cnt[i]), -1)
            if top1 == -1:
                break
            c = min(cnt[top1], repeatLimit-int(len(result) > 0 and result[-1] == top1))
            cnt[top1] -= c
            result.extend([top1]*c)
            top2 = next((j for j in reversed(range(top1)) if cnt[j]), -1)
            if top2 == -1:
                break
            cnt[top2] -= 1
            result.append(top2)
        return "".join([chr(x+ord('a')) for x in result])
