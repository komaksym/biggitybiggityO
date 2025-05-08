# Time:  O(m + n)

import collections


class Solution(object):
    def wordSubsets(self, A, B):
        
        count = collections.Counter()
        for b in B:
            for c, n in list(collections.Counter(b).items()):
                count[c] = max(count[c], n)
        result = []
        for a in A:
            count = collections.Counter(a)
            if all(count[c] >= count[c] for c in count):
                result.append(a)
        return result

