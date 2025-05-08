# Time:  O(n)

import collections


class Solution(object):
    def findLucky(self, arr):
        count = collections.Counter(arr)
        result = -1
        for k, v in count.items():
            if k == v:
                result = max(result, k)
        return result
