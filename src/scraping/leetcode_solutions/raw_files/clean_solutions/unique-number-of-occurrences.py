# Time:  O(n)

import collections


class Solution(object):
    def uniqueOccurrences(self, arr):
        count = collections.Counter(arr)
        lookup = set()
        for v in count.values():
            if v in lookup:
                return False
            lookup.add(v)
        return True


# Time:  O(n)
class Solution2(object):
    def uniqueOccurrences(self, arr):
        count = collections.Counter(arr)
        return len(count) == len(set(count.values()))
