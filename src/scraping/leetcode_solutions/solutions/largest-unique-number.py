# Time:  O(n)

import collections


class Solution(object):
    def largestUniqueNumber(self, A):
        
        A.append(-1)
        return max(k for k,v in list(collections.Counter(A).items()) if v == 1)
