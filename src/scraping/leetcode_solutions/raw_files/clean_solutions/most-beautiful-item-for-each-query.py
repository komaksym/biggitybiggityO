# Time:  O(nlogn + qlogn)

import bisect


class Solution(object):
    def maximumBeauty(self, items, queries):
        items.sort()
        for i in range(len(items)-1):
            items[i+1][1] = max(items[i+1][1], items[i][1])
        result = []
        for q in queries:
            i = bisect.bisect_left(items, [q+1])
            result.append(items[i-1][1] if i else 0)
        return result
