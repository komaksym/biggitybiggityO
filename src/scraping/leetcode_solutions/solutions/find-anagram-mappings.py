# Time:  O(n)

import collections


class Solution(object):
    def anagramMappings(self, A, B):
        
        lookup = collections.defaultdict(collections.deque)
        for i, n in enumerate(B):
            lookup[n].append(i)
        result = []
        for n in A:
            result.append(lookup[n].popleft())
        return result

